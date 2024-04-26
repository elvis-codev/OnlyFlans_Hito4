from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactFormForm, UserForm, TestimonialForm
from .models import Flan, ContactForm, Testimonial
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
import json

# Create your views here.
def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})


@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html',{'flanes':flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            messages.success(request, '¡El formulario se ha enviado con éxito!')
            return redirect('contacto')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})


def exito(request):
    return render(request, 'success.html', {})


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Para poder guardar la contraseña de forma encriptada
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('bienvenido')
    else:
        form = UserForm()

    return render(request, 'registration/registrate.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = '/'


@login_required
def testimonios(request):
    testimonios = Testimonial.objects.all()
    return render(request, 'testimonios.html', {'testimonios': testimonios})


def testimonios(request):
    testimonios = Testimonial.objects.all()
    form = TestimonialForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            testimonio = form.save(commit=False)
            testimonio.usuario = request.user
            testimonio.save()
            messages.success(request, 'Gracias por tu testimonio.')
            return redirect('testimonios')
    return render(request, 'testimonios.html', {'testimonios': testimonios, 'form': form})