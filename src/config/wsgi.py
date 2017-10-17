# -*- coding: utf-8 -*-
"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from local_prod import local_or_prod

local_or_prod, config = local_or_prod()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", config)

application = get_wsgi_application()
