from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, time
from .models import Registro


def solicitar(request):
    
    hora_inicio = time(9, 0)  # 09:00
    hora_fim = time(10, 0)    # 17:00

    # Obtem o horário atual
    hora_atual = datetime.now().time()
    
    if hora_inicio <= hora_atual <= hora_fim:
        return render(request, 'lista/formulario.html',{})
    else:
        return render(request, 'lista/aviso.html',{})




def registros(request):
    
    registros = Registro.objects.all()
    return render(request, 'lista/registros.html',{'registros':registros})

