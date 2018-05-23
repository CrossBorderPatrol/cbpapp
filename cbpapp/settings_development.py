from cbpapp.settings_production import *

DEBUG = bool(int(os.getenv('DEBUG', '0')))

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
