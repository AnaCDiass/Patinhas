from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Endereco(models.Model):
    rua = models.CharField(max_length=100, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"


class Animal(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do animal")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    raca = models.CharField(max_length=50, verbose_name="Raça")
    idade = models.IntegerField(verbose_name="Idade (em anos)")
    sexo = models.CharField(max_length=10, verbose_name="Sexo")
    status = models.CharField(
        max_length=20,
        choices=[('Disponível', 'Disponível'), ('Adotado', 'Adotado')],
        default='Disponível',
        verbose_name="Status"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"


class Adocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal adotado")
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Adotante")
    data = models.DateField(verbose_name="Data da adoção")

    def __str__(self):
        return f"{self.animal} adotado por {self.pessoa}"

    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"


class Doacao(models.Model):
    nome_doador = models.CharField(max_length=100, verbose_name="Nome do doador", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    forma_pagamento = models.CharField(max_length=50, verbose_name="Forma de pagamento")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data da doação")

    def __str__(self):
        return f"R${self.valor:.2f} - {self.forma_pagamento}"


class Campanha(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título da campanha")
    descricao = models.TextField(verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_fim = models.DateField(verbose_name="Data de término")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Campanha"
        verbose_name_plural = "Campanhas"


class Denuncia(models.Model):
    nome_denunciante = models.CharField(max_length=100, verbose_name="Nome do denunciante")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True, null=True)
    descricao = models.TextField(verbose_name="Descrição da denúncia")
    data = models.DateField(auto_now_add=True, verbose_name="Data da denúncia")
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Endereço")

    def __str__(self):
        return f"Denúncia de {self.nome_denunciante} em {self.data}"


class SaudeAnimal(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE, verbose_name="Veterinário")
    data = models.DateField(verbose_name="Data do atendimento")
    observacoes = models.TextField(verbose_name="Observações")

    def __str__(self):
        return f"Saúde de {self.animal} - {self.data}"

    class Meta:
        verbose_name = "Ficha de Saúde"
        verbose_name_plural = "Fichas de Saúde"


class Ocupacao(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome da Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")

    def __str__(self):
        return f"{self.nome} ({self.ocupacao})"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class SaudeAnimal(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    vacina = models.CharField(max_length=100, verbose_name="Vacina")
    data = models.DateField(verbose_name="Data")
    observacoes = models.TextField(blank=True, verbose_name="Observações")

    def __str__(self):
        return f"{self.animal.nome} - {self.vacina} ({self.data})"

    class Meta:
        verbose_name = "Saúde Animal"
        verbose_name_plural = "Saúde Animal"
