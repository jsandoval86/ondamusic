from django.conf.urls import url
from django.contrib import admin

from app.api.views import (
	SongListView,
	SongDetailView,
	PlayListCreateView
)


urlpatterns = [

		# endpoint songs
		url(r'^songs/$', SongListView.as_view(), name="songs_list"),
		url(r'^songs/(?P<pk>\d+)/$', SongDetailView.as_view(), name="songs_detail"),

		# endpoint playlist
		url(r'^play-list/$', PlayListCreateView.as_view(), name="play_list"),
]
