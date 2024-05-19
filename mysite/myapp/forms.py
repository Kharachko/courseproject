# forms.py

from django import forms
from .models import Manga, Chapter

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'author', 'description', 'genres', 'ongoing', 'image_file']
        
class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['manga', 'number', 'title', 'pdf_file']