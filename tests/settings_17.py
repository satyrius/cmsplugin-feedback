# This settings module is for Django 1.7 or higher
from settings import *  # NOQA

# To stop django warn about MIDDLEWARE_CLASSES changed
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
)

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
}
