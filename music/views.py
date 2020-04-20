from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


# Home View
def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'music/home.html', context)


# Detail View
def detail(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id)
    }
    return render(request, 'music/detail.html', context)
