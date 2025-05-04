from typing import io
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from Student.serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
#class StudentApi(APIView):
#    def get(self,request,pk=None,format=None):
#        if pk is not None:
#            Students = Student.objects.get(Id=pk)
#            StudentSerializers = StudentSerializer(Students)
#            return Response(StudentSerializers.data)

#        Students = Student.objects.all()
#        StudentSerializers = StudentSerializer(Students, many=True)
#        return Response(StudentSerializers.data)

class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]