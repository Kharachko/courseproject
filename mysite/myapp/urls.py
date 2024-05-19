from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('manga/<int:manga_id>/', views.indexManga, name='indexManga'),
    path('chapter/<int:id>/', views.chapter_detail, name='chapter_detail'),
    path('catalog/', views.catalog, name='catalog'),
    path('addmanga/', views.add_manga, name='add_manga'),
    path('manga/<int:manga_id>/addchapter/', views.add_chapter, name='addchapter'),
    path('chapter/<int:chapter_id>/edit/', views.edit_chapter, name='editchapter'),
    path('chapter/<int:chapter_id>/delete/', views.delete_chapter, name='deletechapter'),
    path('manga/<int:manga_id>/edit/', views.edit_manga, name='editmanga'),
    path('manga/<int:manga_id>/delete/', views.delete_manga, name='deletemanga'),
]
