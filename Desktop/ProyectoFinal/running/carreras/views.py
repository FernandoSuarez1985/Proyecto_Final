from django.urls import reverse
from django.shortcuts import render
from carreras.models import Carrera, Marathon
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from carreras.forms import Marathon_form
from django.contrib.auth.mixins import LoginRequiredMixin



class List_carrera(ListView):
    model = Carrera
    template_name = 'carreras.html'
    queryset = Carrera.objects.filter(active = True)

class Detail_carrera(DetailView):
    model = Carrera
    template_name = 'carreras/detail_carrera.html'
    queryset = Carrera.objects.filter(active = True)

class Create_carrera(LoginRequiredMixin, CreateView):
    model = Carrera
    template_name = 'carreras/create_carrera.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('carreras/detail_carrera.html',kwargs={'pk':self.object.pk} )

class Delete_carrera(DeleteView):
    model = Carrera
    template_name = 'carreras/delete_carrera.html'
    
    def get_success_url(self):
        return reverse('list_carrera')

class Update_carrera(UpdateView):
    model = Carrera
    template_name = 'carreras/update_carrera.html'
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('carreras/detail_carrera.html', kwargs = {'pk':self.object.pk})

def search_carrera(request):
    carrera = carrera.objects.filter(name__icontains=request.GET['search'])
    if carrera.exists():
        context = {'carrera':carrera}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'search_maraton.html', context = context)


def marathon_list(request):
    marathon = Marathon.objects.filter(active = True)
    context = {'marathon': marathon}
    return render(request, 'maraton/marathon_list.html', context = context)

def marathon_create(request):
    if request.method == 'GET':
        form = Marathon_form()
        context = {'form' : form}
        return render(request, 'maraton/marathon_create.html', context = context)
    else:
        form = Marathon_form(request.POST)
        if form.is_valid():
            new_marathon = Marathon.objects.create(
                name = form.cleaned_data['name'],
                middle_name = form.cleaned_data['middle_name'],
                surname = form.cleaned_data['surname'],
                nickname = form.cleaned_data['nickname'],
                active = form.cleaned_data['active'],
                age = form.cleaned_data['age'],
                number = form.cleaned_data ['number']      
            )
            context = {'new_marathon' : new_marathon}
        return render(request, 'maraton/marathon_create.html', context = context)