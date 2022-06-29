from django import forms
from carreras.models import Carrera, Marathon

class Carrera_form(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'


class Marathon_form(forms.ModelForm):
    class Meta:
        model = Marathon
        fields = '__all__'
