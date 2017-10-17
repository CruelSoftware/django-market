# -*- coding: utf-8 -*-
from django.conf import settings
from functools import wraps

from django.shortcuts import render_to_response

from market.models import (
    Category,
    Object,
    ObjectParam)


# Create your views here.

def object_data(object, params_count=None):
    params_list = []
    obj = {k: getattr(object, k) for k in ('id', 'title', 'price')}
    obj['image'] = object.images.all()[0].image
    obj['images'] = [image.image for image in object.images.all()]
    params = ObjectParam.objects.filter(object=object)[:params_count]
    for param in params:
        param_dict = {'object': param.param.title, 'value': param.value}
        params_list.append(param_dict)
    obj['params'] = params_list
    obj['colors'] = object.colors.all().values_list('html_code', flat=True)

    return obj

def category_data(category):
    return {k: getattr(category, k) for k in ('id', 'title')}

def menu_wrapper(func):
    @wraps(func)
    def wrapped(request, *args, **kwargs):
        template, params = func(*args, **kwargs)
        cat_list = []
        for category in Category.objects.all():
            cat_list.append(category_data(category))
        params.update({'categories': cat_list, 'media': settings.MEDIA_URL})
        return render_to_response(template, params)

    return wrapped


@menu_wrapper
def index():
    objects = []
    for object in Object.objects.all():
        objects.append(object_data(object, 5))
    return 'market/index.html', {'objects': objects}


@menu_wrapper
def category(category_id):
    objects = []
    category = category_data(Category.objects.get(id=category_id))
    for object in Object.objects.filter(category_id=category['id']):
        objects.append(object_data(object, 5))
    return 'market/category.html', {'objects': objects, 'cat': category}


@menu_wrapper
def object(object_id):
    object = object_data(Object.objects.get(id=object_id))
    return 'market/object.html', {'object': object}
