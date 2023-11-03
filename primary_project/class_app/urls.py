from django.urls import path
from . import views

app_name = 'class_app'

urlpatterns = [
    path('clsindex/', views.IndexView.as_view(), name='classindex' ),
    path('clshome/', views.TemView.as_view(), name='clsdex'),
    path('musicianlist/', views.List_View.as_view(), name='musicianlist'),
    path('musician_details/<pk>/', views.MusicianDetail.as_view(), name='musician_details'),
    path('add_musician', views.AddMusician.as_view(), name='add_musician'),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name='update_musician'),
    path('delete_musician/<pk>/', views.DeleteMusician.as_view(), name='delete_musician'),
]
