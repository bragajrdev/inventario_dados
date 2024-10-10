from django.shortcuts import render, redirect
from .models import RegistroTratamento, DadoPessoal, BaseLegal, CriancaAdolescente, DadosSensiveis
from .forms import RegistroTratamentoForm, DadoPessoalForm, BaseLegalForm, CriancaAdolescenteForm, DadosSensiveisForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required



@login_required
def base(request):
    registros = RegistroTratamento.objects.all()
    return render(request, '/base.html', {'registros': registros})

@login_required
def dashboard(request):
    registros = RegistroTratamento.objects.all()
    return render(request, 'core/dashboard.html', {'registros': registros})

@login_required
def criar_registro(request):
    if request.method == 'POST':
        form = RegistroTratamentoForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=True)
            return redirect('adicionar_dados', registro_id=registro.id)
    else:
        form = RegistroTratamentoForm()
    return render(request, 'core/criar_registro.html', {'form': form})

@login_required
def adicionar_dados(request, registro_id):
    registro = RegistroTratamento.objects.get(id=registro_id)
    dados_pessoais = DadoPessoal.objects.filter(registro=registro)
    
    if request.method == 'POST':
        # Verifica se o formulário de dado pessoal foi submetido
        if 'add_dado_pessoal' in request.POST:
            form_dado_pessoal = DadoPessoalForm(request.POST)
            if form_dado_pessoal.is_valid():
                dado = form_dado_pessoal.save(commit=False)
                dado.registro = registro
                dado.save()
                return redirect('adicionar_dados', registro_id=registro.id)
        # Verifica se o formulário de finalização foi submetido
        elif 'finalizar' in request.POST:
            form_base_legal = BaseLegalForm(request.POST, prefix='base_legal')
            form_crianca_adolescente = CriancaAdolescenteForm(request.POST, prefix='crianca_adolescente')
            form_dados_sensiveis = DadosSensiveisForm(request.POST, prefix='dados_sensiveis')

            # Verifica se todos os formulários são válidos antes de salvar
            if (form_base_legal.is_valid() and form_crianca_adolescente.is_valid() and 
                form_dados_sensiveis.is_valid()):
                
                # Salva os modelos relacionados APENAS uma vez
                base_legal_instance, created_base = BaseLegal.objects.get_or_create(
                    registro=registro,
                    defaults=form_base_legal.cleaned_data
                )

                crianca_adolescente_instance, created_crianca = CriancaAdolescente.objects.get_or_create(
                    registro=registro,
                    defaults=form_crianca_adolescente.cleaned_data
                )

                dados_sensiveis_instance, created_sensiveis = DadosSensiveis.objects.get_or_create(
                    registro=registro,
                    defaults=form_dados_sensiveis.cleaned_data
                )

                return redirect('dashboard')  # Redireciona para uma página de sucesso após salvar tudo

    else:
        form_dado_pessoal = DadoPessoalForm()
        form_base_legal = BaseLegalForm(prefix='base_legal')
        form_crianca_adolescente = CriancaAdolescenteForm(prefix='crianca_adolescente')
        form_dados_sensiveis = DadosSensiveisForm(prefix='dados_sensiveis')

    return render(request, 'core/adicionar_dados.html', {
        'form_dado_pessoal': form_dado_pessoal,
        'form_base_legal': form_base_legal,
        'form_crianca_adolescente': form_crianca_adolescente,
        'form_dados_sensiveis': form_dados_sensiveis,
        'registro': registro,
        'dados_pessoais': dados_pessoais,
    })

@login_required
def gerar_pdf(request):
    registros = RegistroTratamento.objects.all()
    template_path = 'core/pdf_template.html'
    context = {'registros': registros}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="InventarioDeDados.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    static_path = os.path.join(settings.BASE_DIR, 'static')

    pisa_status = pisa.CreatePDF(
        html, dest=response,
        link_callback=lambda uri, rel: os.path.join(static_path, uri.replace(settings.STATIC_URL, ""))
    )

    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=500)
    return response
