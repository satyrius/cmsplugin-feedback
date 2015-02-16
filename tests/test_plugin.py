from bs4 import BeautifulSoup
from cms.api import add_plugin
from cms.models import Placeholder
from django.core.urlresolvers import reverse
from django.test import TestCase
from mock import patch
from sekizai.context import SekizaiContext

from cmsplugin_feedback.cms_plugins import FeedbackPlugin, \
    DEFAULT_FORM_FIELDS_ID
from cmsplugin_feedback.forms import FeedbackMessageForm


class CustomMessageForm(FeedbackMessageForm):
    pass


class FeedbackPluginTests(TestCase):
    def setUp(self):
        self.placeholder = Placeholder.objects.create(slot='test')

    def add_plugin(self, **kwargs):
        model_instance = add_plugin(
            self.placeholder,
            FeedbackPlugin,
            'en',
            **kwargs)
        return model_instance

    def render(self, plugin):
        return plugin.render_plugin(SekizaiContext())

    def test_template_render(self):
        plugin = self.add_plugin()
        # Switch on template debug to catch all template errors
        with self.settings(TEMPLATE_DEBUG=True):
            self.render(plugin)

    def test_default_message_form(self):
        model = self.add_plugin()
        plugin = model.get_plugin_class_instance()
        form = plugin.get_message_form()
        self.assertIsInstance(form, FeedbackMessageForm)
        self.assertEqual(form.auto_id, DEFAULT_FORM_FIELDS_ID)

    def test_custom_message_form_by_name(self):
        model = self.add_plugin()
        plugin = model.get_plugin_class_instance()
        with self.settings(CMS_FEEDBACK_FORM='test_plugin.CustomMessageForm'):
            form = plugin.get_message_form()
        self.assertIsInstance(form, CustomMessageForm)
        self.assertEqual(form.auto_id, DEFAULT_FORM_FIELDS_ID)

    @patch.object(FeedbackPlugin, 'get_message_form')
    def test_plugin_context(self, get_form):
        model = self.add_plugin()
        plugin = model.get_plugin_class_instance()
        context = plugin.render({}, model, None)

        self.assertTrue(get_form.called)
        self.assertIn('form', context)
        self.assertEqual(context['form'], get_form.return_value)

    def test_form_action_url(self):
        plugin = self.add_plugin()
        html = self.render(plugin)
        soup = BeautifulSoup(html)
        self.assertEqual(
            soup.form['action'],
            reverse('feedback-form', args=[plugin.id]))
