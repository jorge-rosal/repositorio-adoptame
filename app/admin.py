# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Posts, usuarios,Comment



admin.site.register(Posts)
admin.site.register(Comment)

@admin.register(usuarios)
class usuarios(admin.ModelAdmin):
    list_display = ["name", "Edad", "Telefono", "Email"]
    list_filter = ["name"]


# Register your models here.
