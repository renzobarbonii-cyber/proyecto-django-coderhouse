from django.urls import path, reverse_lazy

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

from . import views


app_name = 'core'


urlpatterns = [

    # INICIO
    path(
        '',
        views.inicio,
        name='inicio'
    ),

    # PÁGINAS PÚBLICAS
    path(
        'acerca-de/',
        views.acerca_de,
        name='acerca_de'
    ),

    path(
        'contacto/',
        views.contacto,
        name='contacto'
    ),

    # USUARIOS
    path(
        'registro/',
        views.registro,
        name='registro'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='core/login.html',
            redirect_authenticated_user=True,
            next_page=reverse_lazy('core:inicio')
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(
            next_page=reverse_lazy('core:inicio')
        ),
        name='logout'
    ),

    path(
        'perfil/',
        views.perfil,
        name='perfil'
    ),

    # BLOG
    path(
        'blog/',
        views.PublicacionListView.as_view(),
        name='lista_publicaciones'
    ),

    path(
        'blog/nueva/',
        views.PublicacionCreateView.as_view(),
        name='crear_publicacion'
    ),

    path(
        'blog/<int:pk>/',
        views.PublicacionDetailView.as_view(),
        name='detalle_publicacion'
    ),

    path(
        'blog/<int:pk>/editar/',
        views.PublicacionUpdateView.as_view(),
        name='editar_publicacion'
    ),

    path(
        'blog/<int:pk>/eliminar/',
        views.PublicacionDeleteView.as_view(),
        name='eliminar_publicacion'
    ),

    # PRODUCTOS
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