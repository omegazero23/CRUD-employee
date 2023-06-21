from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista_prueba/', views.ModePruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path(
        'resume-foundation/',
        views.ResumenFundationView.as_view(),
        name= 'resume_foundation'
    ),

]