import os

from dotenv import load_dotenv
load_dotenv()


URL_HOME = 'https://yandex.ru/'
URL_AUTH = 'https://passport.yandex.ru/auth'
URL_DISK = 'https://disk.yandex.ru/'

mail = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

API_KEY = os.getenv('API_KEY')
URL_JA_DISK = "https://cloud-api.yandex.net/v1/disk"

NAME_TEST_FOLDER_API = 'test_api_folder'
NAME_TEST_DOC_API = 'Файл для копирования.docx'
RENAME_TEST_DOC_API = 'new_name.docx'
NAME_TEST_FOLDER_UI = 'test_ui_folder'
NAME_TEST_DOC_UI = 'test_ui_doc'

NOT_FOUND_STATUS_CODE = 404
CREATED_STATUS_CODE = 201
