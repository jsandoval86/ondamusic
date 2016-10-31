from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	ListCreateAPIView,
)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status

from app.api.serializers import (
	SongSerializer,
	PlayListSerializer
)

from app.models import Song
from app.models import PlayList


class SongListView(ListAPIView):
	"""
	Lista todas las canciones
	"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailView(RetrieveAPIView):
	"""
	Muestra la informacion detallada de una cancion
	"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class PlayListCreateView(ListCreateAPIView):
	"""
	Lista las PlayLists del usuario
	Crea una PlayList 
	"""
	serializer_class = PlayListSerializer
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def get_queryset(self):
		return PlayList.objects.filter(user=self.request.user)

@api_view(['POST'])
def song_add_vote(request, pk):
	"""
	Agrega un voto a una cancion
	"""
	# Buscando cancion
	try:
		pk_song = pk
		song = Song.objects.get(pk=pk_song)
	except Song.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'POST':
		# Aumentar votos de cancion
		song.vote = song.vote + 1
		song.save()

		# Serializar data(cancion)
		serializer = SongSerializer(song)
		song_serialized = serializer.data

		return Response(song_serialized)

