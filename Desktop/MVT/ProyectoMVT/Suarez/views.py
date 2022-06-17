from itertools import product
from multiprocessing import context
from unicodedata import name
from urllib import request
from django.shortcuts import render
from Suarez.models import Familia

# Create your views here.

def tatuajes (request):
    tatuaje_nuevo = Familia.objects.create (
        name = 'figura', 
        descripcion = 'cubo', 
        SKU = 'ASDF1234' 
        )
    context = {'tatuaje_nuevo' : tatuaje_nuevo}
    return render(request, 'tatuajes.html', context=context)