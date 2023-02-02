from django.shortcuts import render

from man.serializers import ManSerializer
from .models import Man
from rest_framework import generics

class ManAPIView(generics.ListAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer