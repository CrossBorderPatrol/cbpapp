import os

from cbpapp.settings import *

DEBUG = bool(int(os.getenv('DEBUG', '0')))

ALLOWED_HOSTS = ['.herokuapp.com']
