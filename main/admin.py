# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
