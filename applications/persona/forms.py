from django import forms
from .models import Empleado

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length = 50)
    apellidos = forms.CharField(max_length = 50)
    departamento = forms.CharField(max_length = 50)
    shortname = forms.CharField(max_length = 20)


class EmpleadoForm(forms.ModelForm):
    """Form definition for Enpleado."""

    class Meta:
        """Meta definition for Enpleadoform."""

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(),

        }
