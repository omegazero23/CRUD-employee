from django.shortcuts import render
from django.views.generic.edit import  FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
	model = Departamento
	template_name = "departamento/lista.html"
	context_object_name = 'departamentos'
 


class NewDepartamentoView(FormView):
	template_name = 'departamento/new_departamento.html'
	form_class = NewDepartamentoForm
	success_url = '/'

	def form_valid(self,form):
		print('¨¨estoy en el form valid*¨¨')
		depa = Departamento(
			name=form.cleaned_data['departamento'],
			short_name=form.cleaned_data['shortname'],
		)
		depa.save()
		nombre = form.cleaned_data['nombre']
		apellidos = form.cleaned_data['apellidos']
		Empleado.objects.create(
			first_name = nombre,
			last_name = apellidos,
			job = '1',
			departamento = depa

		)
		return super(NewDepartamentoView,self).form_valid(form)
	
  