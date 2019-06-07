from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno, Matricula, Professor, Disciplina, Alocacao
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
# httpresponse should be given as parameters the path to the html file of the page
def logout(request):
    request.session.flush()
    return redirect('login')

def index(request):
    if not request.session.has_key('username'):
        messages.warning(request, "não está logado")
        return redirect('login')
    context = {
        'username': request.session['username'],
        'matriculas': Matricula.objects.raw(f"SELECT * FROM siga_matricula WHERE codigo='{request.session['matricula']}'")
    }
    return render(request, 'siga/index.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data.get('aluno_nome')
            s = form.cleaned_data.get('aluno_senha')
            query = f"SELECT * FROM siga_aluno WHERE nome='{n}' AND senha='{s}'"
            print(form, n, s)
            if Aluno.objects.raw(query):
                messages.success(request, f'Login com sucesso, aluno: {n}')
                print(Aluno.objects.raw(query)[0].matricula.codigo)
                request.session['matricula'] = Aluno.objects.raw(query)[0].matricula.codigo
                request.session['username'] = n
                return redirect('index')   
        messages.warning(request, "usuário ou senha inválidos")
    return render(request, 'siga/login.html', {'title': "Login"})