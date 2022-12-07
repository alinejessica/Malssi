from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('altersenha/', views.altersenha, name='altersenha'),
    path('errocadastro/', views.errocadastro, name='errocadastro'),
    path('erroemail/', views.erroemail, name='erroemail'),
    path('erroLogin/', views.erroLogin, name='erroLogin'),
    path('errouser/', views.errouser, name='errouser'),
    path('esqueceusenha/', views.esqueceusenha, name='esqueceusenha'),
    path('produtos/', views.produtos, name='produtos'),
    path('lancamentos/', views.lancamentos, name='lancamentos'),
    path('index/', views.index, name='index'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('politica/', views.politica, name='politica'),
]
