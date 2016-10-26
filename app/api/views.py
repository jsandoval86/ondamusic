from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	ListCreateAPIView,
)

from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail


from app.api.serializers import (
	SongSerializer,
	PlayListSerializer
)

from app.models import Song
from app.models import PlayList
from radio.celery import printText


class SongListView(ListAPIView):

	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailView(RetrieveAPIView):

	queryset = Song.objects.all()
	serializer_class = SongSerializer

class PlayListCreateView(ListCreateAPIView):

	serializer_class = PlayListSerializer
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def get_queryset(self):
		return PlayList.objects.filter(user=self.request.user)