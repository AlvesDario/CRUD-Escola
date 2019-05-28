from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno, Matricula, Professor, Disciplina, Alocacao
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page

# alunos = Aluno.objects.all()
# professor = Professor.objects.all()
# disciplinas = Disciplina.objects.all()
# matriculas = Matricula.objects.all()
# alocacoes = Alocacao.objects.all()

def index(request):
    return render(request, 'siga/index.html')

def aluno(request, aluno_codigo):
    alunos = Aluno.objects.all()
    context = {'title': "login"}
    return render(request, 'siga/alunos.html', context)

def login(request):
    alunos = Aluno.objects.all()
    # print(alunos)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data.get('aluno_nome')
            s = form.cleaned_data.get('aluno_senha')
            print(form, n, s)
            for aluno in alunos:
                if (aluno.nome == n) and (aluno.senha == s):
                    messages.success(request, f'Login com sucesso, aluno: {aluno.nome}')
                    return redirect('aluno/1')
        messages.warning(request, "usuário ou senha inválidos")
    return render(request, 'siga/login.html', {'title': "Login"})

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