from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno, Matricula, Professor, Disciplina, Alocacao
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page

# alunos = Aluno.objects.all()
# professor = Professor.objects.all()
# disciplinas = Disciplina.objects.all()
# matriculas = Matricula.objects.all()
# alocacoes = Alocacao.objects.all()

def index(request):
    return render(request, 'siga/index.html')

def alunos(request):
    return render(request, 'siga/alunos.html', {'title': "login"})

def login(request):
    alunos = Aluno.objects.all()
    # print(alunos)
    if request.method == 'POST':
        print(request.POST)
        for aluno in alunos:
            if (aluno.nome == request.POST.nome[0]):# and (aluno.senha == request.POST.senha[0]):
                messages.success(request, f'Login com sucesso, aluno: {aluno.nome}')
                return redirect('index')
            else:
                return render(request, 'siga/login.html', {'title': "Login", 'errado': True})
    return render(request, 'siga/login.html', {'title': "Login", 'nome':alunos[0].nome,'senha':alunos[0].senha})

# def login(request):
#     return render(request, 'acme/login.html', {'css': 'acme/login.css'})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for user {username}')
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'acme/signup.html', { 'form': form })

# def cars(request):
#     return HttpResponse('cars')

# def offers(request):
#     return HttpResponse('offers')

# def about(request):
#     return HttpResponse('about')

# def account(request):
#     return HttpResponse('account')

# def get_cars(request):
#     carros = Carro.objects.all()
# return render(request, 'acme/carros.html', {'cars': carros})