from datetime import datetime
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render



def familia(request): 
    return HttpResponse ("integrantes")

def fecha(request):
    fecha = datetime.now().date()
    mensaje = f'hoy es {fecha} '    
    return HttpResponse(mensaje)

def probando_template(request):
    context = {
        'fecha' : datetime.now(),
        'nombre':'Fernando',
        'edades': [37,33,41]
    }
    return render(request, 'templates_1.html', context=context )

