==================
cmsplugin-feedback
==================

|ci| |pypi| |status|

.. |ci| image:: https://travis-ci.org/satyrius/cmsplugin-feedback.png?branch=master
    :target: https://travis-ci.org/satyrius/cmsplugin-feedback

.. |pypi| image:: https://pypip.in/version/cmsplugin-feedback/badge.png?text=pypi
    :target: https://pypi.python.org/pypi/cmsplugin-feedback/
    :alt: Latest Version

.. |status| image:: https://pypip.in/status/cmsplugin-feedback/badge.png
    :target: https://pypi.python.org/pypi/cmsplugin-feedback/
    :alt: Development Status

Feedback form plugin for Django CMS [#]_

.. image:: https://cloud.githubusercontent.com/assets/278630/5002184/c4bbe36a-6a0e-11e4-8c5d-024ec11d2c94.png

.. [#] Form style depends on your design, this is just an example. You should customize it with your own CSS.

Requirements
============

Python
------
It works fine and tested under ``Python 2.7``. The following libraries are required

- ``Django`` >=1.5
- ``django-cms`` >= 3.0 (we recommend to use Django CMS 3.0 and higher, contact us if you need prior CMS versions supports and have some issues)
- ``django-simple-captcha`` >= 0.4.1

JavaScript
----------

The feedback form uses ``jQuery`` to post form data asynchronously.
You should take care of this library and include it to your page directly,
or add it to your assets builder, etc.

Installation
============
::

  $ pip install cmsplugin-feedback

Update your ``settings.py`` ::

  INSTALLED_APPS = [
      # django contrib and django cms apps
      'captcha',
      'cmsplugin_feedback',
  ]

Do not forget to include URLs to ``urls.py`` ::

  urlpatterns = patterns('',
      url(r'^captcha/', include('captcha.urls')),
      url(r'^feedback/', include('cmsplugin_feedback.urls')),
      url(r'^', include('cms.urls')),
  )

And to migrate your database ::

  django-admin.py migrate captcha cmsplugin_feedback
  
Notification
------------

Plugin will notify site managers on successful form submit (`MANAGERS` should be configured for Django). You can disable
this behavior in your ``settings.py`` ::

  CMS_FEEDBACK_NOTIFY_MANAGERS = False

And tou can change default email subject ::

  CMS_FEEDBACK_NOTIFY_SUBJECT = 'User feedback'

You can write you own successful submit handler ::

  from cmsplugin_feedback.signals import form_submited
  from django.dispatch import receiver
  
  @receiver(form_submited)
  def submit_handler(sender, message, request, *args, **kwargs):
      pass
  
Roadmap
=======
- Python 3 support
- Both sync and async form posting workflow. To cover number of cases — no javascript (really?); no jquery on the page; you don't want to use async workflow and want to refresh a page.
- Form without captcha (if you dont need it or for registered users)
- Notify site managers about new feedback messages

Changelog
=========
The changelog can be found at `repo's release notes <https://github.com/satyrius/cmsplugin-feedback/releases>`_

Contributing
============
Fork the repo, create a feature branch then send me pull request. Feel free to create new issues or contact me via email.

Translation
-----------
You could also help me to translate `cmsplugin-feedback` to your native language `with Transifex <https://www.transifex.com/projects/p/cmsplugin-feedback/resource/main/>`_
