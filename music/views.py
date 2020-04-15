from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


# Home View
def home(request):
    context = {
        'music': Musician.objects.all()
    }
    return render(request, 'music/home.html', context)
