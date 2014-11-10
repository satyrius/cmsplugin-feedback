from unittest import TestCase
from cmsplugin_feedback.views import JsonResponse


class JsonResponseTest(TestCase):
    def test_from_string(self):
        content = '{"foo": 1}'
        res = JsonResponse(content)
        self.assertEqual(res.content, content)
        self.assertEqual(res['Content-Type'], 'application/json')

    def test_from_dict(self):
        content = {'foo': 1}
        res = JsonResponse(content)
        self.assertEqual(res.content, '{"foo": 1}')
        self.assertEqual(res['Content-Type'], 'application/json')
