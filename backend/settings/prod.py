"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
#APPEND_SLASH=False
import os
import datetime
import dj_database_url
LOGIN_REDIRECT_URL='/'

from django.core.exceptions import ImproperlyConfigured
 
def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SETTINGS_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'verybadsecret!!!'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','localhost','170.244.148.178']

if os.getenv('GAE_APPLICATION',None):
    DEBUGA=True
if os.getenv('SERVER_SOFTWARE','').startswith('Google App Engine'):
    DEBUGA=True
else:
    DEBUGA=True
ACCOUNT_ACTIVATION_DAYS = 7
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # < Per Whitenoise, to disable built in
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'backend.api'
]

#,    'password_reset'
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=86400),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
    'localhost:8000',
    'localhost:3000',
    'localhost',
    'https://viradash.herokuapp.com'
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add dist to
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viradb',
        'USER': 'postgres',
        'PASSWORD': 'newpassword112',
        'HOST': 'localhost',
            'PORT': '5432'
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DATABASE_NAME'),
        'USER': get_env_variable('DATABASE_USER'),
        'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# When Vue Builds, path will be `/static/css/...` so we will have Django Serve
# In Production, it's recommended use an alternative approach such as:
# http://whitenoise.evans.io/en/stable/django.html?highlight=django

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATIC_URL = '/static/'
# Place static in the same location as webpack build files
#STATIC_ROOT = os.path.join(BASE_DIR, 'dist')
STATIC_ROOT = os.path.join(BASE_DIR,  'static')
STATICFILES_DIRS = []


##########
# STATIC #
##########

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


