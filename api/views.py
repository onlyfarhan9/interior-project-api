from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from api.models import Furniture_Details
from api.serializers import Furniture_DetailsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def furniture_details(request):
    furnitures = Furniture_Details.objects.all()
    serializer = Furniture_DetailsSerializer(furnitures,many=True)
    return Response(serializer.data)

    
    


