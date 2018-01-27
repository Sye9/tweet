# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Tweet

from .forms import TweetModelForm

# Register your models here.

class TweetModelAdmin(admin.ModelAdmin):
	form = TweetModelForm

admin.site.register(Tweet, TweetModelAdmin)