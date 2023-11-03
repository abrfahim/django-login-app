from django.urls import path
from login_app import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'login_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('loginpage/', views.login_page, name='login_page'),
    path('userlogin/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)