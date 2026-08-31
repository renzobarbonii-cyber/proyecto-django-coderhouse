from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Producto,
    Perfil,
    Publicacion,
)


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
            'nombre',
            'precio',
            'stock',
        ]


class RegistroForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = [
            'biografia',
            'telefono',
            'ciudad',
        ]


class ContactoForm(forms.Form):

    nombre = forms.CharField(
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        required=True
    )

    asunto = forms.CharField(
        max_length=150,
        required=True
    )

    mensaje = forms.CharField(
        widget=forms.Textarea,
        required=True
    )

    def clean_mensaje(self):

        mensaje = self.cleaned_data['mensaje']

        if len(mensaje) < 10:

            raise forms.ValidationError(
                'El mensaje debe tener al menos 10 caracteres.'
            )

        return mensaje


class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = [
            'titulo',
            'contenido',
        ]