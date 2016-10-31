from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from app.api.views import (
	SongListView,
	SongDetailView,
	song_add_vote,
	PlayListCreateView,
	PlayListDetail,
	play_list_add_song
)


urlpatterns = [

		# Auth jwt
		url(r'^auth/token-jwt/$', obtain_jwt_token, name="auth_jwt"),

		# Social Auth
		url(r'^auth/', include('rest_framework_social_oauth2.urls')),

		# endpoint songs
		url(r'^songs/$', SongListView.as_view(), name="songs_list"),
		url(r'^songs/(?P<pk>\d+)/$', SongDetailView.as_view(), name="songs_detail"),
		url(r'^songs/(?P<pk>\d+)/vote/$', song_add_vote, name="songs_vote"),

		# endpoint playlist
		url(r'^play-list/$', PlayListCreateView.as_view(), name="play_list"),
		url(r'^play-list/(?P<pk>\d+)/$', PlayListDetail.as_view(), name="playlist_detail"),
		url(r'^play-list/(?P<pk>\d+)/add/(?P<song>\d+)/$', play_list_add_song, name="playlist_add_song"),
]
