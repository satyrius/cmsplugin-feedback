export PYTHONPATH := $(CURDIR):$(CURDIR)/tests
export DJANGO_SETTINGS_MODULE := django_settings

messages:
	cd cmsplugin_feedback && django-admin.py makemessages --all

compile:
	cd cmsplugin_feedback && django-admin.py compilemessages

migration:
	django-admin.py schemamigration cmsplugin_feedback --auto || true
