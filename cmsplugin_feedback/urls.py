from django.conf.urls import patterns, url
from cmsplugin_feedback.views import FeedbackView

urlpatterns = patterns('',  # NOQA
    url(r'^form/(?P<plugin>\d+)/?$', FeedbackView.as_view(), name='feedback-form'),
)
