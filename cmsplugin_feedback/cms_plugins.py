from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext as _

from .forms import FeedbackMessageForm
from .models import FeedbackPlugin as Plugin


DEFAULT_FORM_FIELDS_ID = 'contact-%s'
FORM_FIELDS_ID = getattr(settings, 'FEEDBACK_FORM_FIELD_ID',
                         DEFAULT_FORM_FIELDS_ID)

DEFAULT_FORM_CLASS = 'contact-form'
FORM_CLASS = getattr(settings, 'FEEDBACK_FORM_CLASS', DEFAULT_FORM_CLASS)


class FeedbackPlugin(CMSPluginBase):
    model = Plugin
    message_form = FeedbackMessageForm
    name = _('Feedback Plugin')
    render_template = 'cms/plugins/feedback.html'
    form_fields_id = FORM_FIELDS_ID
    form_class = FORM_CLASS

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'form': self.message_form(auto_id=self.form_fields_id),
            'form_class': self.form_class,
        })
        return context

plugin_pool.register_plugin(FeedbackPlugin)
