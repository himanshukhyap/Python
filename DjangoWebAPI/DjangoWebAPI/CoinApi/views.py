from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from CoinApi.models import AssestManager
from CoinApi.serializers import AssestManagerSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, Django!")

@api_view(['GET',"POST"])
def GetAllAssestManager(request):
      if request.method == 'GET':
        #AssestManagers = AssestManager.objects.all()
        #array = []
        #for x in AssestManagers:
        #    data= {
        #        "AssestId":x.AssestId             
        #        }
        #    array.append(data)
        #return Response(array)
        AssestManagers = AssestManager.objects.all()
        AssestManager_serializer = AssestManagerSerializer(AssestManagers, many=True)
        #return JsonResponse(AssestManager_serializer.data, safe=False)
        return Response(AssestManager_serializer.data)

      elif request.method == 'POST':
        AssestManager_serializer = AssestManagerSerializer(data=request.data)
        if AssestManager_serializer.is_valid():
            AssestManager_serializer.save()
            return Response(AssestManager_serializer.data, status=status.HTTP_201_CREATED)
        return Response(AssestManager_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetAssestManagerByAssestId(request, pk):
    try:
        AssestManagers = AssestManager.objects.get(AssestId=pk)
    except AssestManager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      
        AssestManager_serializer = AssestManagerSerializer(AssestManagers)
        return Response(AssestManager_serializer.data)
        #AssestManagers = AssestManager.objects.get(AssestId=pk)
        #AssestManager_serializer = AssestManagerSerializer(AssestManagers, many=True)
        ##return JsonResponse(AssestManager_serializer.data, safe=False)
        #return Response(AssestManager_serializer.data)
     


    



























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