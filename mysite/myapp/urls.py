from django.urls import path
from myapp.views import index,catalog

urlpatterns = [
    #http://127.0.0.1:8000/myapp/hello/
    path('hello', index),
    #http://127.0.0.1:8000/myapp/catalog/
    path('catalog', catalog),
    
]
