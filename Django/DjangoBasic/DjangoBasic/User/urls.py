from django.urls import path

from User.models import Musician
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musician',views.GetMusician.as_view()),   #Class based method 
    path('album',views.GetMusicianDetails,name="Album"),  #function based method
    path('album/<int:pk>',views.GetMusicianDetailsByMusicanId,name="Musiciandetails")
]
