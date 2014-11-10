from django.conf.urls import *  # NOQA

urlpatterns = patterns('',  # NOQA
    url(r'^captcha/', include('captcha.urls')),
    url(r'^feedback/', include('cmsplugin_feedback.urls')),
    url(r'^', include('cms.urls')),
)
