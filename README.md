# url-monitoring
Simple url monitoring app on Python


### Краткое описание:
Простое приложение для чтение Excel файлов, выборке url-адресов и записи в базу полученных данных при обращении к вышеупомянутым адресам. Путь к Excel файлу передается как аргумент скрипту при запуске. В качестве базы данных используется SQLite3, в качестве ORM peewee. Дополнительные настройки прописанны в файле config.py в виде простых переменных. Пристутствует отлов ошибок на разных этапах, ошибки возникшие непосредственно в момент запроса к url логгируются и записываются в json файл.  


### Полезные ссылки:
+ [Peewee](http://docs.peewee-orm.com/en/latest/)
+ [Requests](https://requests.kennethreitz.org/en/master/)
+ [Pandas](https://pandas.pydata.org/pandas-docs/version/0.25/)



### Requirements:
+ certifi==2019.9.11
+ chardet==3.0.4
+ idna==2.8
+ numpy==1.17.2
+ pandas==0.25.1
+ peewee==3.11.2
+ python-dateutil==2.8.0
+ pytz==2019.3
+ requests==2.22.0
+ six==1.12.0
+ urllib3==1.25.6
+ xlrd==1.2.0


### Сборка и запуск:
```
git clone git@github.com:gladunvv/url-monitoring.git
cd url-monitoring/
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd app/
python main.py raw_data.xlsx
```

### License
This project is licensed under the terms of the MIT license
