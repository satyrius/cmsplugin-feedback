from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.importlib import import_module

from .forms import FeedbackMessageForm
from .models import FeedbackPlugin as Plugin


DEFAULT_FORM_FIELDS_ID = 'contact-%s'
FORM_FIELDS_ID = getattr(
    settings, 'CMS_FEEDBACK_FORM_FIELD_ID', DEFAULT_FORM_FIELDS_ID)

DEFAULT_FORM_CLASS = 'contact-form'
FORM_CLASS = getattr(
    settings, 'CMS_FEEDBACK_FORM_CSS_CLASS', DEFAULT_FORM_CLASS)


class FeedbackPlugin(CMSPluginBase):
    model = Plugin
    name = _('Feedback Plugin')
    render_template = 'cms/plugins/feedback.html'

    _form_fields_id = FORM_FIELDS_ID
    _form_class = FORM_CLASS

    @property
    def _message_form(self):
        form = getattr(settings, 'CMS_FEEDBACK_FORM', None)
        if form:
            module, cls = form.rsplit('.', 1)
            return getattr(import_module(module), cls)
        return FeedbackMessageForm

    def get_message_form(self, *args, **kwargs):
        kwargs['auto_id'] = self._form_fields_id
        return self._message_form(*args, **kwargs)

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'form': self.get_message_form(),
            'form_class': self._form_class,
        })
        return context

plugin_pool.register_plugin(FeedbackPlugin)
