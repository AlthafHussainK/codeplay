from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import TravelDiary


def index(request):
    entry = TravelDiary.objects.all()
    context = {'entry' : entry}
    return render(request, 'diary/index.html', context)