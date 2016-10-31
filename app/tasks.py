from __future__ import absolute_import

from celery import task
from django.core.mail import send_mail


@task(name="app.tasks.send_email_new_playlist")
def send_email_new_playlist(user):
	"""
	Enviar email a usuario notificacion de creacion de nueva Playlist
	"""
	send_mail(
		"nueva Playlist creada", 
		"Has creado una nueva Playlist!",
		"Juan Carlos Sandoval Arboleda <juancsandoval86@gmail.com>", 
		[user.email], 
		fail_silently=False
	)