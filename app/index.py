from django.contrib.algoliasearch import AlgoliaIndex

class SongIndex(AlgoliaIndex):
	fields = ('name', 'artist', 'vote')