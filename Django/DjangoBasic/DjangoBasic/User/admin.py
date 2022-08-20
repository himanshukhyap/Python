from django.contrib import admin
from User.models import Album, Musician

admin.site.register(Musician)
admin.site.register(Album)