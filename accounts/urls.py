from django.urls import path
from .views import registro, editar_perfil, ChangePasswordView, perfil, login
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar_password/', ChangePasswordView.as_view(), name='cambiar_password'),
]
