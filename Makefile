export PYTHONPATH := $(CURDIR):$(CURDIR)/tests
export DJANGO_SETTINGS_MODULE := settings_17

messages:
	cd cmsplugin_feedback && django-admin.py makemessages --all

compile:
	cd cmsplugin_feedback && django-admin.py compilemessages

south_migration:
	django-admin.py schemamigration cmsplugin_feedback --auto || true

migration:
	django-admin.py makemigrations cmsplugin_feedback
