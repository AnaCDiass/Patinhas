from django.shortcuts import render, redirect
from django.views import View
from .models import Animal, Campanha, Denuncia, Doacao, Cidade


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AnimaisView(View):
    def get(self, request, *args, **kwargs):
        # Filtra animais com status 'Disponível'
        animais = Animal.objects.filter(status='Disponível')
        return render(request, 'animais.html', {'animais': animais})


class CampanhasView(View):
    def get(self, request, *args, **kwargs):
        campanhas = Campanha.objects.all()
        return render(request, 'campanhas.html', {'campanhas': campanhas})


class DenunciaView(View):
    def get(self, request, *args, **kwargs):
        denuncias = Denuncia.objects.select_related('endereco', 'endereco__cidade').all().order_by('-data')
        return render(request, 'denuncia.html', {'denuncias': denuncias})


class DoacaoView(View):
    def get(self, request, *args, **kwargs):
        doacoes = Doacao.objects.order_by('-id')  # Registros mais recentes primeiro, sem 'ong'
        return render(request, 'doacao.html', {'doacoes': doacoes})
    
class CidadesView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})
