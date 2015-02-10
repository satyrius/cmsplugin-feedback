from django.conf import settings


DEFAULT_FORM_FIELDS_ID = 'contact-%s'
FORM_FIELDS_ID = getattr(
    settings, 'CMS_FEEDBACK_FORM_FIELD_ID', DEFAULT_FORM_FIELDS_ID)

DEFAULT_FORM_CLASS = 'contact-form'
FORM_CLASS = getattr(
    settings, 'CMS_FEEDBACK_FORM_CSS_CLASS', DEFAULT_FORM_CLASS)
