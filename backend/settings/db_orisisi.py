'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'L9DhxkGnPLceglby',
        'PORT': '5432',
        'HOST':'/cloudsql/virameddia:us-east1:virameddiapostgres1'
    }
}

DATABASES['default']['HOST']='/cloudsql/virameddia:us-east1:virameddiapostgres1'
if os.getenv('GAE_INSTANCE'):
    pass
else:
    DATABASES['default']['HOST']='127.0.0.1'
    DATABASES['default']['ENGINE']='django.db.backends.sqlite3'
    DATABASES['default']['NAME']= os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES['default']['PASSWORD']= ''
    DATABASES['default']['PORT']= ''
    DATABASES['default']['USER']= ''


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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'L9DhxkGnPLceglby',
        'PORT': '5432',
        'HOST':'/cloudsql/virameddia:us-east1:virameddiapostgres1'
    }
}
'''