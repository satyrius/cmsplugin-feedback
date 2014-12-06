# This settings module is for Django < 1.7 which uses South for migrations
from settings import *  # NOQA

SOUTH_TESTS_MIGRATE = True
INSTALLED_APPS += [
    'south'
]
