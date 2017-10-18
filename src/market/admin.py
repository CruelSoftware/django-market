# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from market.models import (
    Colors,
    Category,
    Object,
    Param,
    ObjectParam,
    Image,
)

admin.site.register(Colors)
admin.site.register(Category)
admin.site.register(Object)
admin.site.register(Param)
admin.site.register(ObjectParam)
admin.site.register(Image)
