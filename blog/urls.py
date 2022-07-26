from django.urls import path
from .views import crear_posteo

urlpatterns = [
    # path('posteos/', views.ListadoGatos.as_view(), name= "listado_gatos"),
    path('crear-posteo/', crear_posteo , name= "crear_posteo"),
    # path('editar-gato/<int:pk>/', views.EditarGato.as_view(), name= "editar_gato"),
    # path('eliminar-gato/<int:pk>/', views.EliminarGato.as_view(), name= "eliminar_gato"),
    # path('mostrar-gato/<int:pk>/', views.MostrarGato.as_view(), name= "mostrar_gato")
]
   