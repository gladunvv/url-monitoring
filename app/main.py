import pandas as pd
import requests
import sqlite3
import email.utils as eut
import datetime
from models import Monitoring
import json
import config
import os
import sys
import traceback

def get_path_from_args():
    try:
        path = sys.argv[1]
    except IndexError:
        sys.stdout.write('Введите путь до xlsx файла \n')
        sys.exit()
    else:
        read_excel_file(path)

def read_excel_file(path):
    try:
        data = pd.read_excel(path)
    except FileNotFoundError:
        sys.stdout.write('Путь введен не верно \n')
        sys.exit()
    else:
        only_fetch_true_pull(data)

def only_fetch_true_pull(data):
    try:
        data = data[data['fetch'] == 1]
    except KeyError:
        sys.stdout.write('В файле не обнаруженно необходимых метрик \n')
        sys.exit()
    else:
        get_request_in_pull_url(data)

def get_request_in_pull_url(data):
    for index, row in data.iterrows():
        url = row['url']
        label = row['label']
        try:
            response = requests.get(url)
        except Exception as ex:
            exception_type = type(ex).__name__
            exception_value = list(ex.args)
            stack_info = traceback.format_exc()
            errors_dump_load_to_file(url, exception_type, exception_value, stack_info)
        else:
            create_monitoring_object(response, url, label)

def errors_dump_load_to_file(url, exception_type, exception_value, stack_info):
    errors_dict = {
        'url': url,
        'error': {
            'exception_type': exception_type,
            'exception_value': exception_value,
            'stack_info': stack_info
        }
    }
    file_object = open(config.PATH_ERRORS_FILE, 'w')
    json.dump(errors_dict, file_object)

def my_parsedate(text):
    return datetime.datetime(*eut.parsedate(text)[:6])


def create_monitoring_object(response, url, label):
    res_headers = response.headers
    ts = my_parsedate(res_headers['date'])
    response_time = response.elapsed.total_seconds()
    status_code = response.status_code
    try:
        if status_code == 200:
            content_length = res_headers['content-length']
        else:
            content_length = None
    except KeyError:
        content_length = None

    monitoring = Monitoring.create(
        ts=ts,
        url=url,
        label=label,
        response_time=response_time,
        status_code=status_code,
        content_length=content_length
    )

    monitoring.save()

if __name__ == "__main__":
    get_path_from_args()
