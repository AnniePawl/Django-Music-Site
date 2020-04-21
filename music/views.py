from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician
from .models import Album
from .models import Song


# Home View
def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'music/home.html', context)


# Musician Detail View
def musician_detail(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id)
    }
    return render(request, 'music/musician_detail.html', context)


# Album Detail View
def album_detail(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id)
    }
    return render(request, 'music/album_detail.html', context)


# Song Detail View
def song_detail(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id)
    }
    return render(request, 'music/song_detail.html', context)
