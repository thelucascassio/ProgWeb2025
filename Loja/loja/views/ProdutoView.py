from django.http import HttpResponse
from loja.models import Produto

def list_produto_view(request, id=None):
    #carrega informações vindas do navegador (query string)
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    #mostra no console
    if destaque is not None:
        print(destaque)
    if produto is not None:
        print(produto)
    if promocao is not None:
        print(promocao)
    if categoria is not None:
        print(categoria)
    if fabricante is not None:
        print(fabricante)

    #carrega informações vindas do banco de dados
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto=produto)
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)
    
    #mostra no console
    print(produtos)

    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)