from django.contrib import admin

# Register your models here.
from app.models import Song
from app.models import PlayList

admin.site.register(Song)
admin.site.register(PlayList)