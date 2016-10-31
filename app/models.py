from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):

	name = models.CharField(max_length=50, null=False, blank=False)
	artist = models.CharField(max_length=50, null=True,blank=True)
	vote = models.IntegerField(null=True, blank=True, default=0)

	class Meta:
		verbose_name = "Song"
		verbose_name_plural = "Songs"
		ordering = ['-name']

	def __str__(self):
		return u'%s' % (self.name)


class PlayList(models.Model):

	user = models.ForeignKey(User, related_name='playlist')
	name = models.CharField(max_length=50, null=False, blank=False)
	songs = models.ManyToManyField(Song, blank=True)

	class Meta:
		verbose_name = "Play list"
		verbose_name_plural = "Play lists"

	def __str__(self):
			return u'%s' % (self.name)
