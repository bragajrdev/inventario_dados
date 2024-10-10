from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('criar/', views.criar_registro, name='criar_registro'),
    path('adicionar/<int:registro_id>/', views.adicionar_dados, name='adicionar_dados'),
    path('gerar_pdf/', views.gerar_pdf, name='gerar_pdf'),
]
