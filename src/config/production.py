# -*- coding: utf-8 -*-
from .base import *

DATABASES = {
    'default': env.db('DATABASE_URL',
                      default='postgres://django_market:django_market@localhost:5432/django_market'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
