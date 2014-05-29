from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from stations.models import Station
from stations.serializers import StationSerializer



"""
Generic Views
"""

class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all().order_by('school')
    serializer_class = StationSerializer



class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer