from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.
app_name = "persona_app"
class inicioView(TemplateView):
    """VISTA PAGINA DE INICIO"""
    template_name = 'inicio.html'
    


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    paginate_by = 2
    ordering = 'first_name'

    def get_queryset(self):
        print('++++++++')
        palabra_clave = self.request.GET.get('kword','')
        print('++++++++', palabra_clave)
        lista = Empleado.objects.filter(
            full_name__icontains =  palabra_clave
        )
        print('lista resultado:',lista)
        return lista
    #context_object_name = 'lista'


class ListAllEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    model = Empleado
    paginate_by = 10
    ordering = 'first_name'

    #context_object_name = 'lista'


class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
        departamento__short_name = area
        )
        return lista

class ListByJob(ListView):
    template_name = 'persona/list_by_job.html'
    

    def get_queryset(self):
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(
        job = trabajo
        )
        return lista


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('++++++++')
        palabra_clave = self.request.GET.get('kword','')
        print('++++++++', palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado:',lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name= 'habilidades'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('empleado','')
        if palabra_clave.isdigit():
            empleado = Empleado.objects.get(id=palabra_clave)
            empleado = (empleado.habilidades.all())
            return empleado
        else:
            return []


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

        
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del siglo'
        return context



class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm   
    success_url = reverse_lazy('persona_app:empleados_admin')


    def form_valid(self,form):
        #logica
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' +empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado 
    fields= [
    'first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('******************************')
        print('Metodo Post')
        print('******************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request,*args,**kwargs)

    
    def form_valid(self,form):
        #logica
        print('******************************')
        print('Metodo form valid')
        return super(EmpleadoUpdateView,self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')


