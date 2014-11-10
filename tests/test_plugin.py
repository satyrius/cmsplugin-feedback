from bs4 import BeautifulSoup
from cms.api import add_plugin
from cms.models import Placeholder
from django.core.urlresolvers import reverse
from django.test import TestCase

from cmsplugin_feedback.cms_plugins import FeedbackPlugin, \
    DEFAULT_FORM_FIELDS_ID, DEFAULT_FORM_CLASS
from cmsplugin_feedback.forms import FeedbackMessageForm


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

    def test_plugin_context(self):
        model = self.add_plugin()
        plugin = model.get_plugin_class_instance()
        context = plugin.render({}, model, None)

        self.assertIn('form', context)
        self.assertIsInstance(context['form'], FeedbackMessageForm)
        self.assertEqual(context['form'].auto_id, DEFAULT_FORM_FIELDS_ID)

        self.assertIn('form_class', context)
        self.assertEqual(context['form_class'], DEFAULT_FORM_CLASS)

    def test_form_title(self):
        title = 'Feedback Form'
        plugin = self.add_plugin(title=title)
        html = plugin.render_plugin({})
        soup = BeautifulSoup(html)
        self.assertEqual(soup.h1.string, title)

    def test_default_submit_button(self):
        plugin = self.add_plugin()
        self.assertTrue(plugin.submit)
        default = plugin._meta.get_field_by_name('submit')[0].default
        self.assertEqual(plugin.submit, default)
        html = plugin.render_plugin({})
        soup = BeautifulSoup(html)
        self.assertEqual(soup.find(type='submit').string, default)

    def test_submit_button(self):
        text = 'Send'
        plugin = self.add_plugin(submit=text)
        default = plugin._meta.get_field_by_name('submit')[0].default
        self.assertNotEqual(text, default)
        self.assertEqual(plugin.submit, text)
        html = plugin.render_plugin({})
        soup = BeautifulSoup(html)
        self.assertEqual(soup.find(type='submit').string, text)

    def test_form_action_url(self):
        plugin = self.add_plugin()
        html = plugin.render_plugin({})
        soup = BeautifulSoup(html)
        self.assertEqual(
            soup.form['action'],
            reverse('feedback-form', args=[plugin.id]))
