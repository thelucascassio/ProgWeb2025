from django.urls import path
from loja.views.CarrinhoView import create_carrinhoitem_view, list_carrinho_view
urlpatterns = [
    path("", list_carrinho_view, name='list_carrinho'),
    path("<int:produto_id>", create_carrinhoitem_view, name='create_carrinhoitem'),
]