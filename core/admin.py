from django.contrib import admin

from .models import (
    Producto,
    Perfil,
    Publicacion,
)


class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'precio',
        'stock',
    )

    search_fields = (
        'nombre',
    )

    list_filter = (
        'stock',
    )


class PerfilAdmin(admin.ModelAdmin):

    list_display = (
        'usuario',
        'ciudad',
        'telefono',
    )

    search_fields = (
        'usuario__username',
        'ciudad',
    )


class PublicacionAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'autor',
        'fecha_creacion',
    )

    search_fields = (
        'titulo',
        'contenido',
        'autor__username',
    )

    list_filter = (
        'fecha_creacion',
        'autor',
    )


admin.site.register(
    Producto,
    ProductoAdmin
)

admin.site.register(
    Perfil,
    PerfilAdmin
)

admin.site.register(
    Publicacion,
    PublicacionAdmin
)