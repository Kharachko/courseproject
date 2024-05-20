from django.shortcuts import render, get_object_or_404, redirect
from .models import Manga, Chapter
from .forms import MangaForm, ChapterForm
import logging
logger = logging.getLogger(__name__)

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
    manga = chapter.manga
    prev_chapter = Chapter.objects.filter(manga=manga, number__lt=chapter.number).order_by('-number').first()
    next_chapter = Chapter.objects.filter(manga=manga, number__gt=chapter.number).order_by('number').first()

    context = {
        'chapter': chapter,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter
    }
    return render(request, 'myapp/chapter_detail.html', context)

def add_manga(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:index') 
    else:
        form = MangaForm()
    return render(request, 'myapp/addmanga.html', {'form': form})

def add_chapter(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.manga = manga
            chapter.save()
            return redirect('myapp:indexManga', manga_id=manga.id)
        else:
            logger.error("Form errors: %s", form.errors)
    else:
        form = ChapterForm(initial={'manga': manga})
    return render(request, 'myapp/add_chapter.html', {'form': form, 'manga': manga})

def edit_manga(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES, instance=manga)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')  # Повертаємося на головну сторінку після редагування
    else:
        form = MangaForm(instance=manga)
    return render(request, 'myapp/edit_manga.html', {'form': form})

def delete_manga(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    if request.method == 'POST':
        manga.delete()
        return redirect('myapp:index')  # Повертаємося на головну сторінку після видалення
    return render(request, 'myapp/delete_manga.html', {'manga': manga})

def edit_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('myapp:chapter_detail', id=chapter.id)
    else:
        form = ChapterForm(instance=chapter)
    return render(request, 'myapp/edit_chapter.html', {'form': form, 'chapter': chapter})

def delete_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    manga_id = chapter.manga.id
    if request.method == 'POST':
        chapter.delete()
        return redirect('myapp:indexManga', manga_id=manga_id)
    return render(request, 'myapp/delete_chapter.html', {'chapter': chapter})

# def user_profile(request, username):
#     user = get_object_or_404(User, username=username)
#     user_data = {
#         'username': user.username,
#         'email': user.email,
#         'date_joined': user.date_joined,
#     }
#     context = {
#         'user_data': user_data
#     }
#     return render(request, 'myapp/user_profile.html', context)
# views.py

