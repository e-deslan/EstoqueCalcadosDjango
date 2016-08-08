from django.contrib import admin

from .models import Cliente, Funcionario, Venda, Calcado, Estante

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(Calcado)
admin.site.register(Estante)
