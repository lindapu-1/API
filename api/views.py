import json
import os
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
#generics is a class that provides a way to create a list of objects and create a new object
from .models import SustainabilityAction
from .serializers import SustainabilityActionSerializer

JSON_FILE_PATH = '/Users/lindadexiaoaojiao/Desktop/API/sustainability_actions.json'  # Path to the JSON file

class SustainabilityActionListCreateView(generics.ListCreateAPIView):
    queryset = SustainabilityAction.objects.all()
    serializer_class = SustainabilityActionSerializer

    def delete(self, request, *args, **kwargs):
        SustainabilityAction.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#this is a class that provides a way to retrieve, update, and delete a single object
class SustainabilityActionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SustainabilityAction.objects.all()
    serializer_class = SustainabilityActionSerializer
    lookup_field = 'pk'
