from django.http import Http404
from django.shortcuts import render

from .models import Rank, Rikishi
from .utils import get_syllables

def index(request):
  rikishi_list = Rikishi.objects.all()
  context = {
    "rikishi_list": rikishi_list
  }
  return render(request, 'rikishi/index.html', context)

def show(request, rikishi_id):
  try:
    rikishi = Rikishi.objects.get(pk=rikishi_id)
  except Rikishi.DoesNotExist:
    raise Http404("Rikishi does not exist")
  
  rank = Rank(rikishi.highest_rank).label
  syllables = get_syllables(rikishi.shikona_first)
  context = {
    'rikishi': rikishi,
    'rank': rank,
    'syllables': syllables
  }
  return render(request, 'rikishi/show.html', context)

