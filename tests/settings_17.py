from settings import *  # NOQA

# Django 1.7 has its own migrations module
INSTALLED_APPS = filter(lambda app: app != 'south', INSTALLED_APPS)

# To stop django warn about MIDDLEWARE_CLASSES changed
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
)
