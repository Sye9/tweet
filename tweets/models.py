# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tweet(models.Model):
	content 		= models.CharField(max_length=140)
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content