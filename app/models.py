from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Autor")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do Autor")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Editora(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Editora")
    site = models.CharField(max_length=100, verbose_name="Site da Editora")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da Editora")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


class Leitor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Leitor")
    email = models.CharField(max_length=100, verbose_name="Email do Leitor")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do Leitor")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"


class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gênero")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"


class Livro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Livro")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do Livro")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do Livro")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do Livro")

    preco = models.IntegerField(verbose_name="Preço do Livro")
    data_plub = models.DateField(verbose_name="Data de Publicação do Livro")
    status = models.BooleanField(verbose_name="Status do Livro")

    def __str__(self):
        return f'{self.nome}, {self.autor}'
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class Emprestimo(models.Model):
    nome = models.ForeignKey(Leitor, on_delete=models.CASCADE, verbose_name="Reservista")

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro Reservado")

    data_reserva = models.DateField(verbose_name="Data da Reserva")
    data_devolucao = models.DateField(verbose_name="Data da Devolução")

    def __str__(self):
        return f'{self.nome}, {self.livro.nome}, {self.data_reserva}, {self.data_devolucao}'
    
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'