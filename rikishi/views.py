from django.shortcuts import render
from django.http import HttpResponse

from .models import Rikishi

def index(request):
  rikishi_list = Rikishi.objects.all()
  output = ", ".join([rikishi.shikona() for rikishi in rikishi_list])
  return HttpResponse(output)

def show(request, rikishi_id):
  response = "Details for rikishi %s"
  return HttpResponse(response % rikishi_id)

