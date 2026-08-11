from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.inicio,
        name='inicio'
    ),

    path(
        'productos/',
        views.ProductoListView.as_view(),
        name='lista_productos'
    ),

    path(
    'productos/nuevo/',
    views.ProductoCreateView.as_view(),
    name='crear_producto'
    ),

    path(
    'productos/<int:pk>/editar/',
    views.ProductoUpdateView.as_view(),
    name='editar_producto'
    ),

   path(
    'productos/<int:pk>/eliminar/',
    views.ProductoDeleteView.as_view(),
    name='eliminar_producto'
    ),
]
