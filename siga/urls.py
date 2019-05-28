from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('aluno/<aluno_codigo>', views.aluno, name = 'aluno'),
    path('login/', views.login, name = 'login'),
    # path('')
]