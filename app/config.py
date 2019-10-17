import os

NAME_DB = 'database.db'

BASE_DIR = BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RELATIVE_PATH_FOR_DB = ''

PATH_DB = os.path.join(BASE_DIR, RELATIVE_PATH_FOR_DB, NAME_DB)

TIMEOUT = 10

NAME_ERRORS_FILE = 'errors.json'

RELATIVE_PATH_FOR_ERRORS = ''

PATH_ERRORS_FILE = os.path.join(BASE_DIR, RELATIVE_PATH_FOR_ERRORS, NAME_ERRORS_FILE)
