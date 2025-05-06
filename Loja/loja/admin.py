from django.contrib import admin

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao','preco', 'categoria',) #o display só coloca os nomes na criação/edição, enquanto que o fields mostra os campos que são apresentados na tela de edição
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'preco', 'categoria',)
    exclude = ('msgPromocao',)
    search_fields = ('Produto',)

#o fields seria uma implementação mais certeira do que o list display, porque quando definimos o fields, ele só irá mostrar aquilo já definido
# Register your models here.
from .models import * #imporata nossos models
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)