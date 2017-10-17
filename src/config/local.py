# -*- coding: utf-8 -*-
from .base import *


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.

#LOGIN_URL = "/login/"
DEBUG_APPS = [
    'debug_toolbar',
]
INTERNAL_IPS = [
    '127.0.0.1',
    '192.168.33.10',
    '192.168.1.147',
    '192.168.232.1',
    '192.168.38.1',
    '192.168.33.1',
]

INSTALLED_APPS += DEBUG_APPS

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DATABASES = {
    'default': env.db('DATABASE_URL',
                      default='postgres://django_market:django_market@localhost:5432/django_market'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

