from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DEFAULT_FORM_FIELDS_ID = 'contact-%s'
FORM_FIELDS_ID = getattr(
    settings, 'CMS_FEEDBACK_FORM_FIELD_ID', DEFAULT_FORM_FIELDS_ID)

DEFAULT_FORM_CLASS = 'contact-form'
FORM_CLASS = getattr(
    settings, 'CMS_FEEDBACK_FORM_CSS_CLASS', DEFAULT_FORM_CLASS)

NOTIFY_MANAGERS = getattr(
    settings, 'CMS_FEEDBACK_NOTIFY_MANAGERS', True)

DEFAULT_NOTIFY_SUBJECT = _('New feedback')
NOTIFY_SUBJECT = getattr(
    settings, 'CMS_FEEDBACK_NOTIFY_SUBJECT', DEFAULT_NOTIFY_SUBJECT)
