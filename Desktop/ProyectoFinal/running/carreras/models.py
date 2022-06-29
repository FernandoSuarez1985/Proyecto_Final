from distutils.command.upload import upload
from email.mime import image
from unicodedata import category
from django.db import models

def lownst(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text


class Carrera(models.Model):
    name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 10, blank = True, null = True)
    surname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 25)
    active = models.BooleanField(default = True)
    age = models.CharField(max_length = 5)
    number = models.CharField(max_length = 5)
    category = models.ForeignKey('Marathon', on_delete=models.CASCADE, related_name='carreras')
    image = models.ImageField(upload_to = 'carreras', blank = True, null = True)
    
    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        
    def __str__(self):
        return self.name


class Marathon(models.Model):
    name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 10, blank = True, null = True)
    surname = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 25)
    active = models.BooleanField(default = True)
    age = models.CharField(max_length = 5)
    number = models.CharField(max_length = 5)
    
    class Meta:
        verbose_name = 'Maraton'
        verbose_name_plural = 'Maratons'
        
    def __str__(self):
        return self.name


