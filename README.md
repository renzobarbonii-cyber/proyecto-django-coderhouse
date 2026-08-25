# Proyecto Django - Coderhouse

Proyecto desarrollado como práctica del curso de Python y Django de Coderhouse.

La aplicación permite gestionar productos mediante un CRUD completo, realizar búsquedas por nombre, administrar productos desde Django Admin y controlar acciones mediante usuarios, grupos y permisos.

## Funcionalidades

- Listado de productos
- Búsqueda de productos por nombre
- Creación de productos
- Edición de productos
- Eliminación de productos
- CRUD mediante Class-Based Views
- Herencia de templates
- URLs nombradas y namespaces
- Django Admin personalizado
- Sistema de usuarios y grupos
- Sistema de permisos
- Protección de vistas según permisos

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- Git
- GitHub

## Estructura principal del proyecto

```text
PROYECTO/
│
├── config/
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
└── README.md
