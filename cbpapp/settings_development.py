from cbpapp.settings import *

DEBUG = bool(int(os.getenv('DEBUG', '0')))
