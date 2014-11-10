# coding=utf-8
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    email = models.EmailField(_('Email'))
    text = models.TextField(_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)


class FeedbackPlugin(CMSPlugin):
    title = models.CharField(max_length=255)
    submit = models.CharField(
        _('Submit button value'),
        default=_('Submit'),
        max_length=30)
    ok_message = models.TextField(
        _('Success submition message'),
        default='Your message was sent. Thank you for feedback!')

    def __unicode__(self):
        return self.title
