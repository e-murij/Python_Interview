from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'catalog',
        'USER': 'kate',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}