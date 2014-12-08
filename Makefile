export PYTHONPATH := $(CURDIR):$(CURDIR)/tests
export DJANGO_SETTINGS_MODULE := settings

messages:
	cd cmsplugin_feedback && django-admin.py makemessages --all

compile:
	cd cmsplugin_feedback && django-admin.py compilemessages

south_migration:
	DJANGO_SETTINGS_MODULE=settings_south django-admin.py schemamigration cmsplugin_feedback --auto || true

migration:
	DJANGO_SETTINGS_MODULE=settings_17 django-admin.py makemigrations cmsplugin_feedback
