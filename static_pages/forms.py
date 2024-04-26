from django import forms
from .models import ContactForm, Testimonial
from django.contrib.auth.models import User

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name',  'message']

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required', label="Email")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="Pass")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Alias',
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['nombre', 'correo', 'testimonio']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['testimonio']