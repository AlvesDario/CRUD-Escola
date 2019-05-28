from django import forms

class LoginForm(forms.Form):
    aluno_nome = forms.CharField(label='Nome do Aluno', max_length=20)
    aluno_senha = forms.CharField(label='Senha do Aluno', max_length=6)