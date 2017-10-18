# -*- coding: utf-8 -*-
import string
import random
from django.conf import settings

from django.db import models
from django.template.defaultfilters import slugify
from unidecode import unidecode


# Create your models here.

def image_upload_to(self, filename):
    # title = self.alt
    try:
        slug = slugify(unidecode(self.alt))
    except:
        slug = None
    if not slug:
        slug = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
    basename, file_extension = filename.split('.')
    new_filename = '{}images/{}.{}'.format(settings.MEDIA_URL, slug, file_extension)
    return new_filename


class Colors(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, unique=True)
    html_code = models.CharField(max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class Object(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    category = models.ForeignKey(Category)
    colors = models.ManyToManyField(Colors)
    price = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Param(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class ObjectParam(models.Model):
    param = models.ForeignKey(Param)
    object = models.ForeignKey(Object)
    value = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{}/{}'.format(self.object.title, self.value)


class Image(models.Model):
    object = models.ForeignKey(Object, related_name='images')
    image = models.ImageField(upload_to=image_upload_to,
                              null=True,
                              blank=True,
                              width_field="width",
                              height_field="height")
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    alt = models.CharField(max_length=64, null=False, blank=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.alt
