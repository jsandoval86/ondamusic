from rest_framework.serializers import ModelSerializer

from app.models import (
	Song,
	PlayList
)

class SongSerializer(ModelSerializer):

	class Meta:
		model = Song
		fields = ('name', 'artist', 'vote')


class PlayListSerializer(ModelSerializer):

	class Meta:
		model = PlayList
		fields = ('name',)