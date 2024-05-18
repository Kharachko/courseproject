from django.shortcuts import render
from django.http import HttpResponse
from .models import Manga, Chapter

def index(request):
    items = Manga.objects.all()
    context = {
        'items': items
    }
    return render(request, 'myapp/index.html', context)

def indexManga(request, manga_id):
    return HttpResponse("manga id " + str(manga_id))

def catalog(request):
    return render(request, 'myapp/catalog.html')
