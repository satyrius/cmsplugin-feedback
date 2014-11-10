from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from cmsplugin_feedback.cms_plugins import FeedbackPlugin, \
    DEFAULT_FORM_FIELDS_ID, DEFAULT_FORM_CLASS
from cmsplugin_feedback.forms import FeedbackMessageForm


class MypluginTests(TestCase):
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            FeedbackPlugin,
            'en',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)

        self.assertIn('form', context)
        self.assertIsInstance(context['form'], FeedbackMessageForm)
        self.assertEqual(context['form'].auto_id, DEFAULT_FORM_FIELDS_ID)

        self.assertIn('form_class', context)
        self.assertEqual(context['form_class'], DEFAULT_FORM_CLASS)
