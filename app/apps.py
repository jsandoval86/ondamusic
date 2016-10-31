from __future__ import unicode_literals

from django.apps import AppConfig
from django.contrib import algoliasearch

from app.index import SongIndex

class AppConfig(AppConfig):
	name = 'app'

	def ready(self):
		songModel = self.get_model('Song')
		algoliasearch.register(songModel, SongIndex)
