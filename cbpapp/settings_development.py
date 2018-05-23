from cbpapp.settings_production import *

DEBUG = bool(int(os.getenv('DEBUG', '0')))
