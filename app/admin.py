from django.contrib import admin
from .models import *
from django.contrib import admin

admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1  # Número de livros adicionais para adicionar no admin

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Campos que serão exibidos na listagem
    search_fields = ('nome',)  # Campos que serão pesquisados
    inlines = [LivroInline]  # Adiciona a tabela de livros no admin de autores

admin.site.register(Livro)
admin.site.register(Autor, AutorAdmin)
