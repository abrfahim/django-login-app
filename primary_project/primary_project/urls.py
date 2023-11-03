from django.contrib import admin
from django.urls import path, include

# from primary_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('primary_app.urls')),
    path('', include('class_app.urls')),
]
