from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('nueva/', views.crear_moto, name='crear_moto'),
    path('editar/<int:id>/', views.editar_moto, name='editar_moto'),
    path('eliminar/<int:id>/', views.eliminar_moto, name='eliminar_moto'),
]