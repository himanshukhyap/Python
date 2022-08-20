from django.urls import path

from User.models import Musician
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Musician',views.GetMusician,name="Musician"),
    path('Album',views.GetMusicianDetails,name="Album"),
    path('Album/<int:pk>',views.GetMusicianDetailsByMusicanId,name="Musiciandetails")
]
