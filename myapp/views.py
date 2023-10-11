from django.shortcuts import render
from django.http import HttpResponse
from .serializers import AssingnedAuthoritySerializer
from rest_framework.generics import ListAPIView
from .models import AssingnedAuthority, Admin_Details, Alerts, Emergency_Contacts, Department, News_and_Updates
from .models import Precautionary_Advisory, Schemes, Training_Data

def index(request):
    return HttpResponse("<img src = '/static/login.jpg'> ")

class AssingnedAuthorityList(ListAPIView):
  queryset = AssingnedAuthority.objects.all()
  serializer_class = AssingnedAuthoritySerializer
