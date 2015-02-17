from unittest import TestCase

from django.contrib.sites.models import Site
from django.http import HttpRequest
from mock import Mock, patch

import urls  # NOQA
from cmsplugin_feedback.models import Message
from cmsplugin_feedback import signals


class EmailTest(TestCase):
    def setUp(self):
        self.msg = Message.objects.create(
            name='Anton Egorov',
            email='aeg@example.com',
            text='Hello World!')
        self.request = Mock(spec=HttpRequest)

    def test_admin_url(self):
        site = Mock(spec=Site, domain='mysite.com')
        with patch.object(signals, 'get_current_site',
                          return_value=site) as get_site:
            url = signals.get_admin_url(self.msg, self.request)
            get_site.assert_called_once_with(self.request)
            self.assertEqual(
                url, 'http://{s}/admin/cmsplugin_feedback/'
                     'message/{id}/'.format(s=site.domain, id=self.msg.id))

    def test_render_email(self):
        url = 'http://example.com/admin/cmsplugin_feedback/message/1/'
        with patch('cmsplugin_feedback.signals.get_admin_url',
                   return_value=url) as get_url:
            text = signals.render_email(self.msg, self.request)
            get_url.assert_called_once_with(self.msg, self.request)

        self.assertIn(self.msg.name, text)
        self.assertIn(self.msg.text, text)
        self.assertIn(url, text)
