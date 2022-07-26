from django import forms
from ckeditor.fields import RichTextFormField 


class FormPosteo(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    contenido = RichTextField()
    imagen = forms.ImageField()


# class BusquedaGato(forms.Form):
#     apodo = forms.CharField(max_length=30, required=False)


