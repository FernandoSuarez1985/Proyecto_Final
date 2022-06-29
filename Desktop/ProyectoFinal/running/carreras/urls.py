from django.urls import path
from carreras.views import List_carrera, Create_carrera, Detail_carrera, Delete_carrera, Update_carrera, search_carrera
from carreras.views import marathon_list, marathon_create

urlpatterns =[

    path('', List_carrera.as_view(), name = 'Lista_carrera'),
    path('crear-carrera/', Create_carrera.as_view(), name = 'Create_carrera'),
    path('detalle-carrera/<int:pk>/', Detail_carrera.as_view(), name = 'Detail_carrera'),
    path('borrar-carrera/<int:pk>/', Delete_carrera.as_view(), name = 'Delete_carrera'),
    path('actualizar-carrera/<int:pk>/', Update_carrera.as_view(), name = 'Update_carrera'),
    path('buscar-carrera/', search_carrera, name = 'search_maraton'),

    path('listar-maraton/', marathon_list, name = 'marathon_list'),
    path('crear-maraton/', marathon_create, name = 'marathon_create'),   
]

