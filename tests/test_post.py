import json
from cms.api import add_plugin
from cms.models import Placeholder
from django.core.urlresolvers import reverse
from django.test import TestCase
from cmsplugin_feedback.cms_plugins import FeedbackPlugin
from cmsplugin_feedback.views import JsonResponse, VALIDATION_ERROR


class FormPostTest(TestCase):
    def setUp(self):
        placeholder = Placeholder.objects.create(slot='test')
        self.plugin = add_plugin(placeholder, FeedbackPlugin, 'en')
        self.url = reverse('feedback-form', args=[self.plugin.id])

    def post(self, data):
        return self.client.post(
            self.url, data, content_type='application/json')

    def test_post_empty_form(self):
        res = self.post({})

        # Bad Request HTTP response code expected
        self.assertEqual(res.status_code, 400)

        # Decode json data
        self.assertIsInstance(res, JsonResponse)
        content = json.loads(res.content)

        self.assertIn('message', content)
        self.assertEqual(content['message'], unicode(VALIDATION_ERROR))
        self.assertIn('errors', content)
        self.assertIn('name', content['errors'])
        self.assertIn('email', content['errors'])
        self.assertIn('text', content['errors'])
        self.assertIn('captcha', content['errors'])
