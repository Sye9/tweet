# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.urls import reverse

from django.db import models

from .validators import validate_content

# Create your models here.

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
	user 			= models.ForeignKey(User)
	content 		= models.CharField(max_length=140, validators=[validate_content])
	updated 		= models.DateTimeField(auto_now=True)
	timestamp		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs={"pk":self.pk})

	class Meta:
		ordering = ['-updated', '-timestamp']