""" Production Settings """

import os
import dj_database_url
from .base import *



DATABASE_URL = os.environ['DATABASE_URL']

DATABASES={}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


############
# SECURITY #
############

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '')

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']
