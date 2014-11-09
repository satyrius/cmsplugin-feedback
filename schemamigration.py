#!/usr/bin/env python
# coding=utf-8
import sys

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'mptt',
    'cms',
    'cmsplugin_feedback',
    'south',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]


def schemamigration():
    # turn ``schemamigration.py --initial`` into
    # ``manage.py schemamigration cmsplugin_disqus --initial`` and setup the
    # enviroment

    from django.conf import settings
    from django.core.management import ManagementUtility

    settings.configure(
        INSTALLED_APPS=INSTALLED_APPS,
        DATABASES=DATABASES,
        TEMPLATE_CONTEXT_PROCESSORS=TEMPLATE_CONTEXT_PROCESSORS
    )

    argv = list(sys.argv)
    argv.insert(1, 'schemamigration')
    argv.insert(2, 'cmsplugin_feedback')
    utility = ManagementUtility(argv)
    utility.execute()

if __name__ == "__main__":
    schemamigration()
