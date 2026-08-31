from django.shortcuts import render, redirect

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin,
    UserPassesTestMixin,
)

from .models import (
    Producto,
    Perfil,
    Publicacion,
)

from .forms import (
    ProductoForm,
    RegistroForm,
    UsuarioForm,
    PerfilForm,
    ContactoForm,
    PublicacionForm,
)


# PÁGINA DE INICIO
def inicio(request):

    productos = Producto.objects.all()

    contexto = {
        'nombre': 'Renzo',
        'curso': 'Python y Django',
        'edad': 21,
        'productos': productos,
    }

    return render(
        request,
        'core/inicio.html',
        contexto
    )


# PÁGINA ACERCA DE
def acerca_de(request):

    return render(
        request,
        'core/acerca_de.html'
    )


# PÁGINA DE CONTACTO
def contacto(request):

    enviado = False

    if request.method == 'POST':

        form = ContactoForm(
            request.POST
        )

        if form.is_valid():

            enviado = True

            form = ContactoForm()

    else:

        form = ContactoForm()

    contexto = {
        'form': form,
        'enviado': enviado,
    }

    return render(
        request,
        'core/contacto.html',
        contexto
    )


# REGISTRO DE USUARIO
def registro(request):

    if request.method == 'POST':

        form = RegistroForm(
            request.POST
        )

        if form.is_valid():

            usuario = form.save()

            login(
                request,
                usuario
            )

            return redirect(
                'core:inicio'
            )

    else:

        form = RegistroForm()

    contexto = {
        'form': form
    }

    return render(
        request,
        'core/registro.html',
        contexto
    )


# PERFIL DEL USUARIO
@login_required(
    login_url='core:login'
)
def perfil(request):

    perfil_usuario, creado = Perfil.objects.get_or_create(
        usuario=request.user
    )

    if request.method == 'POST':

        usuario_form = UsuarioForm(
            request.POST,
            instance=request.user
        )

        perfil_form = PerfilForm(
            request.POST,
            instance=perfil_usuario
        )

        if (
            usuario_form.is_valid()
            and perfil_form.is_valid()
        ):

            usuario_form.save()
            perfil_form.save()

            return redirect(
                'core:perfil'
            )

    else:

        usuario_form = UsuarioForm(
            instance=request.user
        )

        perfil_form = PerfilForm(
            instance=perfil_usuario
        )

    contexto = {
        'usuario_form': usuario_form,
        'perfil_form': perfil_form,
    }

    return render(
        request,
        'core/perfil.html',
        contexto
    )


# BLOG - LISTAR PUBLICACIONES
class PublicacionListView(ListView):

    model = Publicacion

    template_name = (
        'core/publicaciones.html'
    )

    context_object_name = (
        'publicaciones'
    )

    ordering = [
        '-fecha_creacion'
    ]


# BLOG - VER PUBLICACIÓN
class PublicacionDetailView(DetailView):

    model = Publicacion

    template_name = (
        'core/detalle_publicacion.html'
    )

    context_object_name = (
        'publicacion'
    )


# BLOG - CREAR PUBLICACIÓN
class PublicacionCreateView(
    LoginRequiredMixin,
    CreateView
):

    model = Publicacion

    form_class = PublicacionForm

    template_name = (
        'core/crear_publicacion.html'
    )

    success_url = reverse_lazy(
        'core:lista_publicaciones'
    )

    login_url = reverse_lazy(
        'core:login'
    )

    def form_valid(self, form):

        form.instance.autor = (
            self.request.user
        )

        return super().form_valid(
            form
        )


# BLOG - EDITAR PUBLICACIÓN
class PublicacionUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    model = Publicacion

    form_class = PublicacionForm

    template_name = (
        'core/editar_publicacion.html'
    )

    success_url = reverse_lazy(
        'core:lista_publicaciones'
    )

    login_url = reverse_lazy(
        'core:login'
    )

    def test_func(self):

        publicacion = self.get_object()

        return (
            self.request.user
            == publicacion.autor
        )


# BLOG - ELIMINAR PUBLICACIÓN
class PublicacionDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):

    model = Publicacion

    template_name = (
        'core/eliminar_publicacion.html'
    )

    success_url = reverse_lazy(
        'core:lista_publicaciones'
    )

    login_url = reverse_lazy(
        'core:login'
    )

    def test_func(self):

        publicacion = self.get_object()

        return (
            self.request.user
            == publicacion.autor
        )


# PRODUCTOS - LISTAR Y BUSCAR
class ProductoListView(ListView):

    model = Producto

    template_name = (
        'core/productos.html'
    )

    context_object_name = (
        'productos'
    )

    def get_queryset(self):

        queryset = (
            super().get_queryset()
        )

        query = self.request.GET.get(
            'q',
            ''
        )

        if query:

            queryset = queryset.filter(
                nombre__icontains=query
            )

        return queryset


# PRODUCTOS - CREAR
class ProductoCreateView(
    PermissionRequiredMixin,
    CreateView
):

    model = Producto

    form_class = ProductoForm

    template_name = (
        'core/crear_producto.html'
    )

    success_url = reverse_lazy(
        'core:lista_productos'
    )

    permission_required = (
        'core.add_producto'
    )

    login_url = reverse_lazy(
        'core:login'
    )


# PRODUCTOS - EDITAR
class ProductoUpdateView(
    PermissionRequiredMixin,
    UpdateView
):

    model = Producto

    form_class = ProductoForm

    template_name = (
        'core/editar_producto.html'
    )

    success_url = reverse_lazy(
        'core:lista_productos'
    )

    permission_required = (
        'core.change_producto'
    )

    login_url = reverse_lazy(
        'core:login'
    )


# PRODUCTOS - ELIMINAR
class ProductoDeleteView(
    PermissionRequiredMixin,
    DeleteView
):

    model = Producto

    template_name = (
        'core/eliminar_producto.html'
    )

    success_url = reverse_lazy(
        'core:lista_productos'
    )

    permission_required = (
        'core.delete_producto'
    )

    login_url = reverse_lazy(
        'core:login'
    )