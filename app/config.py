import os

class Config(object):
    SECRET_KEY = os.environ.get('YANDEX_LYCEUM_SECRET_KEY')