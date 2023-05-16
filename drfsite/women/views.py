from django.shortcuts import render

from rest_framework import generics
# Create your views here.
from serializer import WomenSerializer
from .models import Women


class WomenAPIview(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
