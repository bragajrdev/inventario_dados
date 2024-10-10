from django.db import models
from django.utils import timezone

class RegistroTratamento(models.Model):
    atividade_de_tratamento = models.CharField(max_length=255)
    secretaria_ou_departamento = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.atividade_de_tratamento} - {self.secretaria_ou_departamento}'

class DadoPessoal(models.Model):
    registro = models.ForeignKey(RegistroTratamento, related_name='dados_pessoais', on_delete=models.CASCADE)
    tipo_dado = models.CharField(max_length=200, choices=[
        ('nome', 'Nome'),
        ('cpf', 'CPF'),
        ('endereco', 'Endereço'),
        ('telefone', 'Telefone'),
        ('email', 'E-mail'),
        ('dados_saude', 'Dados de Saúde'),
    ])

    def __str__(self):
        return self.tipo_dado

class BaseLegal(models.Model):
    registro = models.ForeignKey(RegistroTratamento, related_name='base_legal', on_delete=models.CASCADE)
    base_legal = models.CharField(max_length=260, choices=[
        ('consentimento','Consentimento'), ('cumprimento_obrigacao','Cumprimento de Obrigação Legal'),
        ('execucao_politicas','Execução de Políticas Públicas'),('interesse_legitimo','Interesse Legítimo'),
        ('exercicio_direito','Exercício Regular de Direito em Processo Judicial/Administrativo'), ('protecao_vida','Proteção da Vida ou da Incolumidade Física do Titular'),
    ])

    def __str__(self):
        return self.base_legal

class CriancaAdolescente(models.Model):
    registro = models.ForeignKey(RegistroTratamento, related_name='crianca_adolescente', on_delete=models.CASCADE)
    crianca_adolescente = models.CharField(max_length=100, choices=[
        ('sim','Sim'), ('nao','Não'),
    ])

    def __str__(self):
        return self.crianca_adolescente

class DadosSensiveis(models.Model):
    registro = models.ForeignKey(RegistroTratamento, related_name='dados_sensiveis', on_delete=models.CASCADE)
    dados_sensiveis = models.CharField(max_length=100, choices=[
        ('sim','Sim'), ('nao','Não'),
    ])

    def __str__(self):
        return self.dados_sensiveis
