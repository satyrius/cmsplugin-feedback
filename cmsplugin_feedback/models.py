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
    # Keep this model for future plugin customization options
    pass
