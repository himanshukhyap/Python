
from django.conf import urls
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.routers import DefaultRouter 
from CoinApi import views 
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
router = router.register("CoinApi",views.AssestManagerViewSet,basename="AssestManager")
urlpatterns = [ 
    path("coin/",include(router,urls))
    #path('', views.AssestManagerViewSet,name="GetAllAssestManager"),
    #path('<str:pk>', views.GetAssestByAssestId,name="GetAssestManagerByAssestId")

    #path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #path(r'^api/tutorials/published$', views.tutorial_list_published)
]
urlpatterns = format_suffix_patterns(urlpatterns)