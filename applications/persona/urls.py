from django.urls import path
from . import views

app_name= 'persona_app'

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view(),name='empleados_all'),
    path('list-by-area/<shortname>/', views.ListByAreaEmpleado.as_view(),name='empleados_area'),
    path('listar-empleados-admin/', views.ListAllEmpleadosAdmin.as_view(),name='empleados_admin'),
    path('list-by-job/<job>/', views.ListByJob.as_view()),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(),name='empleado_detalle'),
    path('add-empleado/',views.EmpleadoCreateView.as_view(),name='empleado_add'),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
        ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='update'
        ),
    path(
        'delete/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='delete'
        ),
    path(
        '',
        views.inicioView.as_view(),
        name = 'Inicio', 

    ),
]