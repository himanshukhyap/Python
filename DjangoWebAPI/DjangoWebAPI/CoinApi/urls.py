
from django.urls import path 
from CoinApi import views 
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [ 
    path('', views.GetAllAssestManager,name="GetAllAssestManager"),
    path('<str:pk>', views.GetAssestManagerByAssestId,name="GetAssestManagerByAssestId")

    #path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #path(r'^api/tutorials/published$', views.tutorial_list_published)
]
urlpatterns = format_suffix_patterns(urlpatterns)