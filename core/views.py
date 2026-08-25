from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Producto
from .forms import ProductoForm


# PÁGINA DE INICIO
def inicio(request):

    productos = Producto.objects.all()

    contexto = {
        'nombre': 'Renzo',
        'curso': 'Python y Django',
        'edad': 21,
        'productos': productos,
    }

    return render(request, 'core/inicio.html', contexto)


# READ - LISTAR Y BUSCAR PRODUCTOS
class ProductoListView(ListView):
    model = Producto
    template_name = 'core/productos.html'
    context_object_name = 'productos'

    def get_queryset(self):

        queryset = super().get_queryset()

        query = self.request.GET.get('q', '')

        if query:
            queryset = queryset.filter(
                nombre__icontains=query
            )

        return queryset


# CREATE - CREAR PRODUCTO
class ProductoCreateView(PermissionRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/crear_producto.html'
    success_url = reverse_lazy('core:lista_productos')

    permission_required = 'core.add_producto'


# UPDATE - EDITAR PRODUCTO
class ProductoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/editar_producto.html'
    success_url = reverse_lazy('core:lista_productos')

    permission_required = 'core.change_producto'


# DELETE - ELIMINAR PRODUCTO
class ProductoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Producto
    template_name = 'core/eliminar_producto.html'
    success_url = reverse_lazy('core:lista_productos')

    permission_required = 'core.delete_producto'