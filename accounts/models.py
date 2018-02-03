from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.


class UserProfile(models.Model):
	user 		= models.OneToOneField(User, related_name='profile')
	following 	= models.ManyToManyField(User, blank=True, related_name='followed_by')

	def __str__(self):
		return str(self.following.all().count())