from cbpapp.settings import *

DEBUG = False

ALLOWED_HOSTS = ['cpbapp.herokuapp.com']

PROJECT_APPS = [
    'core',
    'portal',
]

INSTALLED_APPS = INSTALLED_APPS + PROJECT_APPS
