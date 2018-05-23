import os

from cbpapp.settings_production import *

DEBUG = bool(int(os.getenv('DEBUG', '0')))

ALLOWED_HOSTS = ['.herokuapp.com']
