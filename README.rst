=================
django-crowd-auth
=================

Django backend authentication using Crowd's REST API. Feature compatible with https://github.com/Linaro/django-crowd-rest-backend

Python 2.7 and Python 3.5

Configure
=========

* Add :code:`crowd_auth` to :code:`INSTALLED_APPS` inside settings file,
* Add :code:`crowd_auth.Backend` to :code:`AUTHENTICATION_BACKENDS` inside settings file.


Settings
--------

* :code:`AUTH_CROWD_APPLICATION_PASSWORD`
* :code:`AUTH_CROWD_APPLICATION_USER`
* :code:`AUTH_CROWD_SERVER_REST_URI`

      Required settings, will be used connect to Crowd server on the given application and given URL resource.

* :code:`AUTH_CROWD_ALWAYS_UPDATE_USER = False # default`
      Whether you want to sync django users from Crowd attributes. If you use any form of group-based autorization/permission checking, you'd rather have this as True (default). In particular, :code:`AUTH_CROWD_STAFF_GROUP` & :code:`AUTH_CROWD_SUPERUSER_GROUP` settings depend on this.


* :code:`AUTH_CROWD_CREATE_GROUPS = False # default`
      Whether you want to sync all user's Crowd groups into Django This setting is considered only if :code:`AUTH_CROWD_ALWAYS_UPDATE_GROUPS = True`. If this is True, then all user's groups in Crowd will be synced to Django (so, effectively, you'll be able to check Crowd group memberships using Django API). If set to False (default), no groups will be created by backend, and only groups already existing in Django will be considered (i.e. user group membership in Django will be updated to intersection of user's Crowd groups and all available Django groups).

      You'd rather have this as True (default). In particular, :code:`AUTH_CROWD_STAFF_GROUP` & :code:`AUTH_CROWD_SUPERUSER_GROUP` settings depend on this.

* :code:`AUTH_CROWD_STAFF_GROUP = None  # default`
      Django user will get staff flag when Crowd user is in given Crowd group

* :code:`AUTH_CROWD_SUPERUSER_GROUP = None  # default`
      Django user will get superuser flag when Crowd user is in given Crowd group Note that superuser group member does not imply staff membership and vice versa (make sure you read Django docs to understand the difference).
