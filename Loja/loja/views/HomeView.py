#from django.http import HttpResponse
from django.shortcuts import render
from loja.models import Produto

def home_view(request):
    #return HttpResponse('<h1>Olá mundo!</h1>')
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    contexto = {'produtos': produtos}
    return render(request, template_name='home/home.html', context=contexto, status=200)
