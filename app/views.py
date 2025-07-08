from django.shortcuts import render, redirect
from django.views import View
from .models import Animal, Campanha, Denuncia, Doacao, Cidade, Endereco, Pessoa, Ocupacao, SaudeAnimal


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
        return render(request, 'denuncias.html', {'denuncias': denuncias})


class DoacaoView(View):
    def get(self, request, *args, **kwargs):
        doacoes = Doacao.objects.order_by('-id') 
        return render(request, 'doacao.html', {'doacoes': doacoes})
    
class CidadesView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

class EnderecosView(View):
    def get(self, request, *args, **kwargs):
        enderecos = Endereco.objects.select_related('cidade').all()
        return render(request, 'enderecos.html', {'enderecos': enderecos})


class PessoasView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas': pessoas})


class OcupacaoView(View):
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

    def post(self, request):
        nome = request.POST.get('nome')
        if nome:
            Ocupacao.objects.create(nome=nome)
        return redirect('ocupacao')
    
class SaudeAnimalView(View):
    def get(self, request):
        registros = SaudeAnimal.objects.all()
        return render(request, 'saudeanimal.html', {'registros': registros})