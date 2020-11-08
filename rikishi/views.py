from django.http import Http404
from django.shortcuts import render

from .models import Rank, Rikishi
from .utils import get_syllabic_anagrams

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
  anagrams = get_syllabic_anagrams(rikishi.shikona_first)
  context = {
    'rikishi': rikishi,
    'rank': rank,
    'anagrams': anagrams
  }
  return render(request, 'rikishi/show.html', context)

