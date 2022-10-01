from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("",views.StudentApi,basename="Student")

urlpatterns = [
    path('', include(router.urls)),
   
   
  
]
#urlpatterns = [
#    path('', views.StudentApi.as_view()),
#    path('<int:pk>', views.StudentApi.as_view()),
  
#]
