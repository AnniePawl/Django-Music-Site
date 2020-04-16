from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician


# Home View
def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'music/home.html', context)
