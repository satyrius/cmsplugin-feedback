import datetime as dt
import json

from cms.api import add_plugin
from cms.models import Placeholder
from django.core.urlresolvers import reverse
from django.test import TestCase
from freezegun import freeze_time
from mock import patch

from cmsplugin_feedback.cms_plugins import FeedbackPlugin
from cmsplugin_feedback.forms import FeedbackMessageForm
from cmsplugin_feedback.models import Message
from cmsplugin_feedback.views import JsonResponse, VALIDATION_ERROR, OK


class FormPostTest(TestCase):
    def setUp(self):
        placeholder = Placeholder.objects.create(slot='test')
        self.plugin = add_plugin(placeholder, FeedbackPlugin, 'en')
        self.url = reverse('feedback-form', args=[self.plugin.id])

    def post(self, data, expect_code=None):
        res = self.client.post(self.url, data)
        self.assertIsInstance(res, JsonResponse)
        content = json.loads(res.content)
        if expect_code is not None:
            self.assertEqual(res.status_code, expect_code, content)
        return content

    def test_post_empty_form(self):
        res = self.post({}, expect_code=400)

        # The overall message error expected
        self.assertIn('message', res)
        self.assertEqual(res['message'], unicode(VALIDATION_ERROR))

        # Django form error should be included
        self.assertIn('errors', res)
        self.assertIn('name', res['errors'])
        self.assertIn('email', res['errors'])
        self.assertIn('text', res['errors'])
        self.assertIn('captcha', res['errors'])

    @patch.object(FeedbackMessageForm, 'save')
    def test_captcha(self, save):
        data = {
            'name': 'Anton Egorov',
            'email': 'aeg@example.com',
            'text': 'Thank you!',
        }
        res = self.post(data, expect_code=400)

        # We have only captcha validation failed
        self.assertIn('errors', res)
        self.assertEqual(res['errors'].keys(), ['captcha'], res['errors'])

        # The new captcha sould be suggested
        self.assertIn('captcha', res)
        captcha = res['captcha']
        self.assertIn('img', captcha)
        self.assertIn('key', captcha)
        self.assertFalse(save.called)

        # Post with captha passed emulation
        data['captcha_0'] = captcha['key']
        data['captcha_1'] = 'passed'
        res = self.post(data, expect_code=200)
        self.assertNotIn('errors', res)
        self.assertNotIn('captcha', res)
        self.assertIn('message', res)
        self.assertEqual(res['message'], OK)
        self.assertTrue(save.called)

    @freeze_time('2014-11-10 23:44:00')
    def test_save_message(self):
        data = {
            'name': 'Anton Egorov',
            'email': 'aeg@example.com',
            'text': 'Thank you!',
            'captcha_0': 'captcha_key',
            'captcha_1': 'passed',
        }
        res = self.post(data, expect_code=200)
        self.assertIn('id', res)
        message = Message.objects.get(pk=res['id'])
        self.assertEqual(message.name, data['name'])
        self.assertEqual(message.email, data['email'])
        self.assertEqual(message.text, data['text'])
        self.assertEqual(message.created_at, dt.datetime.now())
