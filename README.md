# inventario_dados
Projeto em Django de Inventário e Mapeamento de Dados Pessoais

1) Instalar o Python e o Pip;
2) Vai até a pasta do projeto para criar e ativar um ambiente virtual (venv)

comando: python3 -m venv myenv

3) Ativar o ambiente virtual:

MacOS/Linux: source myenv/bin/activate

Windows: myenv\Scripts\activate


4) Instalar o Django e lib xhtml2pdf

Comando: pip install Django e pip install xhtml2pdf


5) Fazer as migrações de banco de dados:

comando: python3 manage.py makemigrations
comando: python3 manage.py migrate

6) Criar um superusuario para o Django Admin:

comando: python manage.py createsuperuser

7) Rodar o Servidor de Desenvolvimento:

Comando: python3 manage.py runserver


Vai rodar na porta: 8000
URL: http://127.0.0.1:8000
