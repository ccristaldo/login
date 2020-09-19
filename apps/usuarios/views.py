from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView

from .models import Usuario
from .forms import SignUpForm


class SignUpView(CreateView):
    model = Usuario
    form_class = SignUpForm
  
    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''

        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'usuarios/bienvenida.html'



class SignInView(LoginView):
    template_name = 'usuarios/login.html'


class SignOutView(LogoutView):
    pass