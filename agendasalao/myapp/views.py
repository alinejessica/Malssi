from django.shortcuts import render

# Create your views here.
def inicio(request):
    data = {}
    return render(request, 'INDES.html', data)

def home(request):
    data = {}
    return render(request, 'home.html', data)

def login(request):
    data = {}
    return render(request, 'Loginprincipal.html', data)

def cadastro(request):
    data = {}
    return render(request, 'CADASTRO.html', data)

def altersenha(request):
    data = {}
    return render(request, 'altersenha.html', data)

def salvarsenha(request):
    data = {}
    return render(request, 'altersenha.html', data)
    
def errocadastro(request):
    data = {}
    return render(request, 'errocadastro.html', data)
    
def erroemail(request):
    data = {}
    return render(request, 'erroemail.html', data)

def erroLogin(request):
    data = {}
    return render(request, 'erroLogin.html', data)
    
def errouser(request):
    data = {}
    return render(request, 'errouser.html', data)

def esqueceusenha(request):
    data = {}
    return render(request, 'esqueceusenha.html', data)

def produtos(request):
    data = {}
    return render(request, 'HISTORIA.html', data)

def lancamentos(request):
    data = {}
    return render(request, 'LANÇAMENTOS.html', data)

def logout(request):
    data = {}
    return render(request, 'logout.html', data)

def profile(request):
    data = {}
    return render(request, 'profile.html', data)

def suceslogin(request):
    data = {}
    return render(request, 'suceslogin.html', data)
       
def index(request):
    data = {}
    return render(request, 'index.html', data)

def agendamento(request):
    data = {}
    return render(request, 'AGENDAMENTO.html', data)


def politica(request):
    data = {}
    return render(request, 'politica.html')

