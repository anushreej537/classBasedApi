from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# views classs ki subclass hai apiview
# Create your views here.

class StudentAPI(APIView):
    def get(self,request,pk=None):
        id = pk
        if id is not None:
            obj = Student.objects.get(id=id)
            serializer = StudentSerializer(obj)
            return Response(serializer.data)
        obj = Student.objects.all()
        serializer = StudentSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # obj = Student.objects.all()
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        id = pk
        if id is not None:
            try:
                obj = Student.objects.get(id=id)
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Student.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
