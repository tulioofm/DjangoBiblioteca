from django.shortcuts import render
from . models import *

def consulta(request):
    consultas = {
        'consultas': Livro.objects.all()
    }

    return render(request, 'consulta/consulta.html', consultas)

def reserva(request):
    if request.POST:
        nova_reserva = Emprestimo()
        nova_reserva.data_emprestimo = request.POST.get('data')
        nova_reserva.data_devolucao = request.POST.get('data2')
        try:
            leitor = Leitores.objects.get(pk = request.POST.get('leitor'))
            livro = Livro.objects.get(pk = request.POST.get('livro'))
            nova_reserva.leitor = leitor
            nova_reserva.livro = livro
            nova_reserva.save()
        except Leitores.DoesNotExist:
            print("Leitor não encontrado")
        except Livro.DoesNotExist:
            print("Livro não encontrado")
        except Exception as e:
            print("Erro de integridade", e)
    reservas = {
        'leitor': Leitores.objects.all(),
        'livro': Livro.objects.all(),
    }

    return render(request, 'reserva/reserva.html', reservas)

def categoria(request):
    categoria = {
        'categoria': Categoria.objects.all()
    }

    return render(request, 'categoria/categoria.html', categoria)

def autor(request):
    autor = {
        'autor': Autor.objects.all()
    }

    return render(request, 'autor/autor.html', autor)

def editora(request):
    editora = {
        'editora': Editora.objects.all()
    }

    return render(request, 'editora/editora.html', editora)
# Create your views here.
