from django.shortcuts import render, get_object_or_404
from .models import Manga, Chapter

def index(request):
    items = Manga.objects.all()
    context = {
        'items': items
    }
    return render(request, 'myapp/index.html', context)

def indexManga(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    chapters = manga.chapters.all()
    context = {
        'manga': manga,
        'chapters': chapters
    }
    return render(request, 'myapp/manga.html', context)

def catalog(request):
    return render(request, 'myapp/catalog.html')

def chapter_detail(request, id):
    chapter = get_object_or_404(Chapter, id=id)
    context = {
        'chapter': chapter
    }
    return render(request, 'myapp/chapter_detail.html', context)
