from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from datetime import datetime

from .forms import BusquedaGato, FormPosteo
from .models import Posteo

# class ListadoGatos(ListView):
#     model = Post
#     template_name = 'gato/listado_gatos.html'

#     def get_queryset(self):
#         apodo = self.request.GET.get("apodo", "")
#         if apodo:
#             object_list = self.model.objects.filter(apodo__icontains=apodo)
#         else: 
#             object_list = self.model.objects.all()

#         return object_list

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = BusquedaGato()

#         return context 


def crear_posteo(request): 
    
    if request.method == "POST":
        form = FormPosteo(request.POST) 

        if form.is_valid():
            data = form.cleaned_data

            posteo = Posteo(
                titulo=data.get("titulo"), 
                subtitulo=data.get("subtitulo"), 
                contenido=data.get("contenido"), 
                autor=data.get("autor"), 
                fecha_creacion=datetime.now(),
                imagen=data.get("imagen")
                )
            posteo.save()
            
            return redirect("listado_posteos")

        else:
            return render(request, 'blog/crear_posteo.html', {"form": form})  
    
    form_posteo = FormPosteo

    return render(request, 'blog/crear_posteo.html', {"form": form_posteo})  
    
    
# class EditarGato(LoginRequiredMixin, UpdateView):
#     model = Gato
#     template_name = 'gato/editar_gato.html'
#     success_url = '/mascotas/gatos'
#     fields = ['apodo', 'edad','fecha_creacion']


# class EliminarGato(LoginRequiredMixin, DeleteView):
#     model = Gato
#     template_name = 'gato/eliminar_gato.html'
#     success_url = '/mascotas/gatos'


# class MostrarGato(DetailView):  
#     model = Gato
#     template_name = 'gato/mostrar_gato.html' 

# @login_required
# def editar_perro(request, id):

#     perro = Perro.objects.get(id=id) 

#     if request.method == "POST":
#         form = FormPerro(request.POST) 

#         if form.is_valid():
#             perro.nombre = form.cleaned_data.get("nombre")
#             perro.edad = form.cleaned_data.get("edad")
#             perro.descripcion = form.cleaned_data.get("descripcion")
#             perro.fecha_creacion = form.cleaned_data.get("fecha_creacion")
#             perro.save()

#             return redirect("listado_perros")

#         else:
#             return render(request, 'perro/editar_perro.html', {"form": form, "perro":perro})  
    
#     form_perro = FormPerro(
#         initial={
#             "nombre": perro.nombre, 
#             "edad": perro.edad, 
#             "descripcion": perro.descripcion, 
#             "fecha_creacion": perro.fecha_creacion
#             })

#     return render(request, 'perro/editar_perro.html', {"form": form_perro, "perro":perro})  

  
#     # return redirect("listado_perros")
    
# @login_required
# def eliminar_perro(request, id):

#     perro = Perro.objects.get(id=id)
#     perro.delete() 

#     return redirect("listado_perros") 
