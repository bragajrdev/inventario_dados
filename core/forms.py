from django import forms
from .models import RegistroTratamento, DadoPessoal, BaseLegal, CriancaAdolescente, DadosSensiveis

class RegistroTratamentoForm(forms.ModelForm):
    class Meta:
        model = RegistroTratamento
        fields = ['atividade_de_tratamento', 'secretaria_ou_departamento']

class DadoPessoalForm(forms.ModelForm):
    class Meta:
        model = DadoPessoal
        fields = ['tipo_dado']

class BaseLegalForm(forms.ModelForm):
    class Meta:
        model = BaseLegal
        fields = ['base_legal']

class CriancaAdolescenteForm(forms.ModelForm):
    class Meta:
        model = CriancaAdolescente
        fields = ['crianca_adolescente']

class DadosSensiveisForm(forms.ModelForm):
    class Meta:
        model = DadosSensiveis
        fields = ['dados_sensiveis']
