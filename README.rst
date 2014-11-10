cmsplugin-feedback
================== 
.. image:: https://travis-ci.org/satyrius/cmsplugin-feedback.svg?branch=master

Feedback form plugin for Django CMS. WARNING, this is under development!

Requirements
------------
* Django>=1.5,<=1.7
* django-cms>=3.0
* django-simple-captcha>=0.4.1

Installation
------------
This library is under development and is not published on *pipi*, so you have to install it from repository by branch name, tag or commit hash ::

  $ pip install -e git@github.com:satyrius/cmsplugin-feedback.git@master#egg=cmsplugin_feedback
  
Update your ``settings.py`` ::

  INSTALLED_APPS = [
      # django contrib and django cms apps
      'captcha',
      'cmsplugin_feedback',
  ]
  
Do not forget to include urls to ``urls.py`` ::

  urlpatterns = patterns('',
      url(r'^feedback/', include('cmsplugin_feedback.urls')),
      url(r'^', include('cms.urls')),
  )

And to migrate your database ::

  django-admin.py migrate captcha cmsplugin_feedback
  
Contributing
------------
Fork the repo, create a feature branch then send me pull request. Feel free to create new issues or contact me using email.
