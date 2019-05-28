from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('alunos/', views.alunos, name = 'alunos'),
    path('login/', views.login, name = 'login'),
    # path('')
]