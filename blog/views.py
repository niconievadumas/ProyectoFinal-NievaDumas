from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from datetime import datetime
from .forms import BusquedaPosteo, FormPosteo
from .models import Posteo
from django.contrib.auth.decorators import login_required



class ListadoPosteos(ListView):
    model = Posteo 
    # queryset = self.model.objects.order_by('titulo')
    template_name = 'blog/listado_posteos.html'
    paginate_by = 5

    def get_queryset(self):
        titulo = self.request.GET.get("titulo", "")
        if titulo:
            object_list = self.model.objects.filter(titulo__icontains=titulo).order_by('-fecha_creacion')
        else: 
            object_list = self.model.objects.all().order_by('-fecha_creacion')
            
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaPosteo()

        return context 

@login_required
def crear_posteo(request): 
    
    if request.method == "POST":
        form = FormPosteo(request.POST, request.FILES) 

        if form.is_valid():
            data = form.cleaned_data

            posteo = Posteo(
                titulo=data.get("titulo").title(), 
                subtitulo=data.get("subtitulo").capitalize(), 
                contenido=data.get("contenido").capitalize(), 
                autor= request.user,
                fecha_creacion=datetime.now(),
                imagen=data.get("imagen")
                )
            posteo.save()
            
            return redirect("listado_posteos")

        else:
            return render(request, 'blog/crear_posteo.html', {"form": form})  
    
    form_posteo = FormPosteo

    return render(request, 'blog/crear_posteo.html', {"form": form_posteo})  
    
    
@login_required
def editar_posteo(request, id):

    posteo = Posteo.objects.get(id=id) 

    if request.method == "POST":
        form = FormPosteo(request.POST, request.FILES) 

        if form.is_valid():
            data = form.cleaned_data
            posteo.titulo = data.get("titulo").title()
            posteo.subtitulo = data.get("subtitulo").capitalize()
            posteo.contenido = data.get("contenido").capitalize()
            posteo.imagen = data.get("imagen") if data.get("imagen") else posteo.imagen
            posteo.fecha_creacion = datetime.now()
            
            posteo.save()

            return redirect("listado_posteos")

        else:
            return render(request, 'blog/editar_posteo.html', {"form": form, "posteo":posteo})  
    
    form_posteo = FormPosteo(
        initial={
            "titulo": posteo.titulo, 
            "subtitulo": posteo.subtitulo, 
            "contenido": posteo.contenido, 
            "imagen": posteo.imagen 
            })

    return render(request, 'blog/editar_posteo.html', {"form": form_posteo, "posteo":posteo})  


class EliminarPosteo(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = 'blog/eliminar_posteo.html'
    success_url = '/blog/listado_posteos'


class MostrarPosteo(DetailView):  
    model = Posteo
    template_name = 'blog/posteo.html' 




