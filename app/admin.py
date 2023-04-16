from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    search_fields=('conteudo', 'data')  
    list_display = ['id', 'conteudo', 'data',]
    list_filter = ('conteudo', 'data')