from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('logout/', views.logout, name = 'logout'),
    path('', views.login, name = 'login'),
]