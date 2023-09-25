from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Entrada, Autor

def lista_entradas(request): 
    entradas = Entrada.objects.all() 
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas}) 

def entradas_por_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    entradas = Entrada.objects.filter(autor=autor)
    return render(request, 'blog/entradas_por_autor.html', {'autor': autor, 'entradas': entradas})
