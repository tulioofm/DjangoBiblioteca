from django.db import models
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.site}'
    
class Editora(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    data_publicacao = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.autor.nome}'
    
class Leitores(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    data_emprestimo = models.DateTimeField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    leitor = models.ForeignKey(Leitores, on_delete=models.CASCADE)
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f'{self.data_emprestimo} - {self.data_devolucao} {self.livro}'