from django.contrib import admin
from .models import Registro, Configuracao


class RegistroAdmin(admin.ModelAdmin):
    
    list_display = ('matricula', 'nome', 'email', 'contra', 'data_almoco')

admin.site.register(Registro, RegistroAdmin)
admin.site.register(Configuracao)
