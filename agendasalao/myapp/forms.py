from django import forms
from .models import Usuario, agendamento


class LoginForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'senha', ]


class addAgendamentoForm(forms.ModelForm):
    class Meta:
        model = agendamento
        fields = ['data_agendamento', 'horario_agendamento','funcionario_id', 'email', 'senha', 'telefone', 'nome', ]


class editMetaForm(forms.ModelForm):
    class Meta:
        model = Procedimento 
        fields = ['descricao', 'data_proced', 'tempo_proced', 'valor']
