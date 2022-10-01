from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ImageWord
from .serializers import ImageWordSerializer


# Create your views here.
def homepage(request):
    return HttpResponse("Home")

class ImageWordViewSet(ModelViewSet):
    queryset = ImageWord.objects.all()
    serializer_class = ImageWordSerializer
    