DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'mptt',
    'cms',
    'cmsplugin_feedback',
    'south',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]

SECRET_KEY = 'ji2r2iGkZqJVbWDhXrgDKDR2qG#mmtvBZXPXDugA4H)KFLwLHy'

SOUTH_TESTS_MIGRATE = True
