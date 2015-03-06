from django.conf.urls import *  # NOQA
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',  # NOQA
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^feedback/', include('cmsplugin_feedback.urls')),
    url(r'^', include('cms.urls')),
)
