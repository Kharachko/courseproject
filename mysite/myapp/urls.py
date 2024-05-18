from django.urls import path
from myapp.views import index,catalog,indexManga

urlpatterns = [
    #http://127.0.0.1:8000/myapp/hello
    path('hello', index),
    path('hello/<int:manga_id>', indexManga),
    #http://127.0.0.1:8000/myapp/catalog
    path('catalog', catalog),
    
]
