# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import index, category, object

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'category/(?P<category_id>\d+)/$', category, name='category'),
    url(r'object/(?P<object_id>\d+)/$', object, name='object'),
]
