# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'primary_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('addalbum/', views.album_form, name='album_form'),
    path('addmusician/', views.musician_form, name='musician_form'),
    path('albumlist/<int:artist_id>/', views.album_list, name= 'album_list'),
    path('edit/<int:artist_id>/', views.edit_artist, name = 'edit_artist'),
    path('editalbum/<int:album_id>/', views.edit_album, name = 'edit_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_musician/<int:artist_id>/', views.delete_Musician, name='delete_Musician')
    
]

