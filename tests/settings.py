LANGUAGE_CODE = 'en'
SECRET_KEY = 'ji2r2iGkZqJVbWDhXrgDKDR2qG#mmtvBZXPXDugA4H)KFLwLHy'
SITE_ID = 1
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nologcapture']
ROOT_URLCONF = 'urls'
CAPTCHA_TEST_MODE = True

STATIC_ROOT = '/tmp/cmsplugin_feedback/static/'
MEDIA_ROOT = '/tmp/cmsplugin_feedback/media/'

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
    'django_nose',
    'captcha',
    'cms',
    'mptt',
    'sekizai',
    'cmsplugin_feedback',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]
