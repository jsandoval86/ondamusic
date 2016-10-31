from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	ListCreateAPIView,
)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators  import api_view
from rest_framework.decorators  import permission_classes
from rest_framework.decorators  import authentication_classes
from rest_framework.response import Response
from rest_framework import status

from app.api.permissions import IsOwnerOnly
from app.api.serializers import (
	SongSerializer,
	PlayListSerializer
)

from app.models import Song
from app.models import PlayList
from app.tasks import print_text


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
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		print_text.apply_async(countdown=5)

	def get_queryset(self):
		return PlayList.objects.filter(user=self.request.user)

class PlayListDetail(RetrieveAPIView):
	"""
	Detalle un PlayList
	"""
	queryset = PlayList.objects.all()
	serializer_class = PlayListSerializer
	permission_classes = (IsOwnerOnly, )


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


@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def play_list_add_song(request, pk, song):
	"""
	Agrega una cancion a un playlist
	"""
	# Buscando playlist y cancion
	try:
		pk_play_list = pk
		pk_song = song

		play_list = PlayList.objects.get(pk=pk_play_list)
		song = Song.objects.get(pk=pk_song)

	except PlayList.DoesNotExist, Song.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	# Validar que usuario sea propietario de la playlist
	if play_list.user.id != request.user.id:
		return Response({"detail": "You do not have permission to perform this action."})

	if request.method == 'POST':
		# Agregar cancion a playlist
		play_list.songs.add(song)

		# Serializar playlist
		serializer = PlayListSerializer(play_list)
		play_list_serialized = serializer.data

		# Respuesta
		return Response(play_list_serialized)

