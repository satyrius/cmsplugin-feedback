from django.conf import settings
from django.utils.translation import ugettext_lazy as _

NOTIFY_MANAGERS = getattr(
    settings, 'CMS_FEEDBACK_NOTIFY_MANAGERS', True)

DEFAULT_NOTIFY_SUBJECT = _('New feedback')
NOTIFY_SUBJECT = getattr(
    settings, 'CMS_FEEDBACK_NOTIFY_SUBJECT', DEFAULT_NOTIFY_SUBJECT)
