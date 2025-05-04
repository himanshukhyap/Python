import json
from django.shortcuts import render
from django.http.response import  HttpResponseNotFound, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from CoinApi.models import AssestDetail, AssestManager
from CoinApi.serializers import AssestDetailSerializer, AssestManagerSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import viewsets
#def index(request):
#    return HttpResponse("Hello, Django!")


#def GetAllAssestManager(request):
#      if request.method == 'GET':
    
#        AssestManagers = AssestManager.objects.all()
#        AssestManager_serializer = AssestManagerSerializer(AssestManagers, many=True)
#        return JsonResponse(AssestManager_serializer.data,safe=False)
     

class AssestManagerViewSet(viewsets.ModelViewSet):
    AssestManagers = AssestManager.objects.all()
    AssestManager_serializer = AssestManagerSerializer


def GetAssestDetailsByAssestId(request, pk):

    try:
       AssestDetails = AssestDetail.objects.get(pk=pk)
    except AssestDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      
        AssestDetail_serializer = AssestDetailSerializer(AssestDetails)
        
        return JsonResponse(AssestDetail_serializer.data, safe=False)
     

#def GetAssestByAssestId(request, pk):

#    try:
#        AssestManagers = AssestManager.objects.get(pk=pk)
#    except AssestManager.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    try:
#        AssestDetails = AssestDetail.objects.get(AssestId=pk)
#    except AssestDetails.DoesNotExist:
#        return HttpResponseNotFound()

#    if request.method == 'GET':
      
#        AssestManager_serializer = AssestManagerSerializer(AssestManagers)
#        AssestDetail_serializer = AssestDetailSerializer(AssestDetails)
#        res = {**AssestManager_serializer.data,**AssestDetail_serializer.data}
#        return JsonResponse(res,safe=False)
     
       
     


    



























    #    if request.method == 'GET':
    #    serializer = SnippetSerializer(snippet)
    #    return Response(serializer.data)

    #elif request.method == 'PUT':
    #    serializer = SnippetSerializer(snippet, data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #elif request.method == 'DELETE':
    #    snippet.delete()
    #    return Response(status=status.HTTP_204_NO_CONTENT)