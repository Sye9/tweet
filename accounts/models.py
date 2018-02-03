from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class UserProfileManager(models.Manager):
	user_for_related_fields = True
	def all(self):
		qs = self.get_queryset().all()
		try:
			if self.instance:
				qs = qs.exclude(user=self.instance)
			return qs
		except:
			pass
		return qs

class UserProfile(models.Model):
	user 		= models.OneToOneField(User, related_name='profile')
	following 	= models.ManyToManyField(User, blank=True, related_name='followed_by')

	objects 	= UserProfileManager()

	def __str__(self):
		return str(self.following.all().count())

	def get_following(self):
		users = self.following.all()
		return users.exclude(username=self.user.username)