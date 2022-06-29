from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from running.views import index, contact, login_view, logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('carreras/', include('carreras.urls')),
    path('contact/', contact, name='contacto'),
    path('login/', login_view, name='login'),

    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),

] + static(settings.MEDIA_URL, docuement_root = settings.MEDIA_ROOT)

