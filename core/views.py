from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Producto
from .forms import ProductoForm


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inicio')

    else:
        form = ProductoForm()

    contexto = {
        'form': form
    }

    return render(request, 'core/crear_producto.html', contexto)


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            form.save()
            return redirect('inicio')

    else:
        form = ProductoForm(instance=producto)

    contexto = {
        'form': form,
        'producto': producto
    }

    return render(request, 'core/editar_producto.html', contexto)


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')

    contexto = {
        'producto': producto
    }

    return render(request, 'core/eliminar_producto.html', contexto)


def inicio(request):
    productos = Producto.objects.all()

    contexto = {
        'nombre': 'Renzo',
        'curso': 'Python y Django',
        'edad': 21,
        'productos': productos,
    }

    return render(request, 'core/inicio.html', contexto)


class ProductoListView(ListView):
    model = Producto
    template_name = 'core/productos.html'
    context_object_name = 'productos'


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/crear_producto.html'
    success_url = reverse_lazy('lista_productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'core/editar_producto.html'
    success_url = reverse_lazy('lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'core/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')