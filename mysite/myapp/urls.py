from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.index, name='hello'),
    path('hello/<int:manga_id>/', views.indexManga, name='helloManga'),
    path('manga/<int:manga_id>/', views.indexManga, name='indexManga'),
    path('catalog/', views.catalog, name='catalog'),
    path('chapter/<int:id>/', views.chapter_detail, name='chapter_detail'),  # Подання для перегляду окремих глав
]
