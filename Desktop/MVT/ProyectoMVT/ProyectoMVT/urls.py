
from django.contrib import admin
from django.urls import path
from ProyectoMVT.views import familia, fecha, probando_template
from Suarez.views import tatuajes 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/',familia, name = 'familia'),
    path('fecha/',fecha, name = 'fecha'),
    path('probando_template/',probando_template, name = 'probando_template'),
    path('tatuajes/',tatuajes, name = 'tatuajes'),
    

]
 