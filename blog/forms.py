from django import forms
from ckeditor.fields import RichTextFormField 


class FormPosteo(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    contenido = RichTextFormField()
    imagen = forms.ImageField(required=False)


class BusquedaPosteo(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)


