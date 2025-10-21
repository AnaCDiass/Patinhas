from django.contrib import admin
from .models import (
    Cidade, Endereco, Animal, Adocao, Doacao,
    Campanha, Denuncia, SaudeAnimal, Ocupacao, Pessoa
)

# ---------- INLINES ----------
class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 1

class AdocaoInline(admin.TabularInline):
    model = Adocao
    extra = 1

class DoacaoInline(admin.TabularInline):
    model = Doacao
    extra = 1

class DenunciaInline(admin.TabularInline):
    model = Denuncia
    extra = 1

class SaudeAnimalInline(admin.TabularInline):
    model = SaudeAnimal
    extra = 1


# ---------- MODEL ADMINS ----------
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "uf")
    search_fields = ("nome", "uf")
    inlines = [EnderecoInline]   # Endereços vinculados à cidade


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ocupacao", "cidade", "cpf", "telefone", "email")
    search_fields = ("nome", "cpf", "ocupacao__nome", "cidade__nome")
    inlines = [AdocaoInline, DoacaoInline, DenunciaInline, SaudeAnimalInline]  
    # Pessoa pode estar ligada a adoções, doações, denúncias e saúde animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "raca", "idade", "sexo", "status")
    search_fields = ("nome", "raca", "tipo")
    inlines = [AdocaoInline, SaudeAnimalInline]  
    # Animal tem histórico de adoções e de saúde


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ("rua", "numero", "bairro", "cidade")
    search_fields = ("rua", "bairro", "cidade__nome")
    # sem inline de denúncia aqui


@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_inicio", "data_fim")
    search_fields = ("titulo",)


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ("animal", "pessoa", "data")
    search_fields = ("animal__nome", "pessoa__nome")


@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ("pessoa", "valor", "forma_pagamento", "data")
    search_fields = ("pessoa__nome",)


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ("pessoa", "endereco", "data")
    search_fields = ("pessoa__nome", "endereco__rua")


@admin.register(SaudeAnimal)
class SaudeAnimalAdmin(admin.ModelAdmin):
    list_display = ("animal", "pessoa", "data")
    search_fields = ("animal__nome", "pessoa__nome")
