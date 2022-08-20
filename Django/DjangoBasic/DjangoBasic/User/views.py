from os import altsep
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from User.models import Album, Musician
from User.serializers import AlbumSerializer, MusicianSerializer
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json
from rest_framework.response import Response

def index(request):
     template = loader.get_template('FirstHtml.html')
     return HttpResponse(template.render())

def GetMusician(request):
     #return HttpResponse("Hello world!")
     if request.method == 'GET':
         Musicians = Musician.objects.all()
         Mserializer = MusicianSerializer(Musicians, many=True)
         return JsonResponse(Mserializer.data, safe=False)

def GetMusicianDetails(request):
     #return HttpResponse("Hello world!")
     if request.method == 'GET':
         Albums = Album.objects.all()
         Aserializer = AlbumSerializer(Albums, many=True)
         return JsonResponse(Aserializer.data, safe=False)




def GetMusicianDetailsByMusicanId(request,pk):

    try:
        Albums = Album.objects.get(pk=pk)
        Musicians = Musician.objects.get(pk=pk)
    except Album.DoesNotExist:
        return HttpResponse(status=404)

     #return HttpResponse("Hello world!")
    if request.method == 'GET':  
         Aserializer = AlbumSerializer(Albums )
         Mserializer = MusicianSerializer(Musicians)
         return JsonResponse({**Mserializer.data,**Aserializer.data}, safe=False)


       
