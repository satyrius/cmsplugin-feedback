# coding=utf-8
import json

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from cms.models import CMSPlugin
from django.views.generic import View
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from .signals import form_submited


VALIDATION_ERROR = _('Validation error')
OK = _('Your message was sent. Thank you!')


class JsonResponse(HttpResponse):
    def __init__(self, content, *args, **kwargs):
        if isinstance(content, dict):
            content = json.dumps(content)
        super(JsonResponse, self).__init__(
            content, content_type='application/json', *args, **kwargs)


class FeedbackView(View):
    def post(self, request, plugin, *args, **kwargs):
        cms_plugin = CMSPlugin.objects.get(pk=plugin)
        model, plugin = cms_plugin.get_plugin_instance()
        form = plugin.get_message_form(self.request.POST)

        if not form.is_valid():
            new_captcha = CaptchaStore.generate_key()
            return JsonResponse({
                'message': unicode(VALIDATION_ERROR),
                'errors': form.errors,
                'captcha': {
                    'key': new_captcha,
                    'img': captcha_image_url(new_captcha),
                },
            }, status=400)
        form.save()
        form_submited.send(self, message=form.instance, request=request)
        return JsonResponse({
            'message': unicode(OK),
            'id': form.instance.id,
        })
