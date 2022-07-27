from django.urls import path
from .views import EliminarPosteo, ListadoPosteos, MostrarPosteo, crear_posteo, editar_posteo

urlpatterns = [
    path('listado_posteos/', ListadoPosteos.as_view(), name= "listado_posteos"),
    path('posteo/<int:pk>/', MostrarPosteo.as_view(), name= "posteo"),
    path('crear-posteo/', crear_posteo , name= "crear_posteo"),
    path('editar-posteo/<int:id>/', editar_posteo, name= "editar_posteo"),
    path('eliminar-posteo/<int:pk>/', EliminarPosteo.as_view(), name= "eliminar_posteo"),
]
   