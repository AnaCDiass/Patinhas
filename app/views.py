from django.shortcuts import render, redirect
from django.views import View
from app.views import *
from .models import Animal, Campanha, Denuncia, ONG, Doacao;



class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class AnimaisView(View):
    def get(self, request, *args, **kwargs):
        # Corrigido para filtrar por status 'Disponível'
        animais = Animal.objects.filter(status='Disponível')
        return render(request, 'animais.html', {'animais': animais})

class CampanhasView(View):
    def get(self, request, *args, **kwargs):
        campanhas = Campanha.objects.all()
        return render(request, 'campanhas.html', {'campanhas': campanhas})

class DenunciaView(View):
    def get(self, request, *args, **kwargs):
        ongs = ONG.objects.all()
        denuncias = Denuncia.objects.all().order_by('-data')  # Mostra as mais recentes primeiro
        return render(request, 'denuncia.html', {'ongs': ongs, 'denuncias': denuncias})

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome_denunciante')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        descricao = request.POST.get('descricao')
        ong_id = request.POST.get('ong')

        ong = ONG.objects.filter(id=ong_id).first()

        Denuncia.objects.create(
            nome_denunciante=nome,
            email=email,
            telefone=telefone,
            descricao=descricao,
            ong=ong
        )

        # Se quiser, dá pra adicionar mensagem de sucesso aqui (com messages framework)
        return redirect('denuncia')


class SobreView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'sobre.html')

class ContatoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contato.html')

class DoacaoView(View):
    def get(self, request, *args, **kwargs):
        ongs = ONG.objects.all()  # Mostrar no template para escolher ONG
        return render(request, 'doacao.html', {'ongs': ongs})

    def post(self, request, *args, **kwargs):
        nome_doador = request.POST.get('nome_doador')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        valor = request.POST.get('valor')
        forma_pagamento = request.POST.get('forma_pagamento')
        ong_id = request.POST.get('ong')

        ong = ONG.objects.filter(id=ong_id).first()

        Doacao.objects.create(
            nome_doador=nome_doador,
            email=email,
            telefone=telefone,
            valor=valor,
            forma_pagamento=forma_pagamento,
            ong=ong
        )
        # Pode adicionar mensagem de sucesso aqui também
        return redirect('doacao')
