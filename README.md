# Proyecto Django - Coderhouse

Proyecto final desarrollado con Python y Django como parte del curso de Coderhouse.

La aplicación consiste en una plataforma web que integra gestión de productos, usuarios, perfiles y publicaciones de blog.

## 🌐 Proyecto online

La aplicación se encuentra desplegada en Render:

https://proyecto-django-coderhouse.onrender.com

---

## 🚀 Funcionalidades

### Usuarios

- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Perfil editable
- Sistema de autenticación de Django

### Blog

- Listado de publicaciones
- Visualización individual de publicaciones
- Creación de publicaciones
- Edición de publicaciones
- Eliminación de publicaciones
- Autor asignado automáticamente
- Solo el autor puede editar o eliminar su publicación

### Productos

- Listado de productos
- Búsqueda por nombre
- Creación de productos
- Edición de productos
- Eliminación de productos
- Sistema de permisos por usuario

### Páginas públicas

- Inicio
- Productos
- Blog
- Acerca de
- Contacto

### Formularios

El proyecto utiliza Django Forms y ModelForms para:

- Registro de usuarios
- Edición de perfiles
- Gestión de productos
- Gestión de publicaciones
- Formulario de contacto

El formulario de contacto incluye validación personalizada.

### Administración

La aplicación utiliza Django Admin para administrar:

- Usuarios
- Grupos
- Permisos
- Productos
- Perfiles
- Publicaciones

---

## 🔐 Permisos

Se implementaron diferentes niveles de acceso.

Los permisos de productos utilizan el sistema de permisos de Django.

En las publicaciones del blog, cada usuario puede editar o eliminar únicamente sus propias publicaciones.

---

## 🎨 Diseño

La aplicación utiliza HTML y CSS personalizado.

Incluye:

- Diseño responsive
- Navbar
- Cards
- Formularios estilizados
- Página de inicio personalizada
- Diseño para productos y publicaciones
- Adaptación para dispositivos móviles

---

## 🛠️ Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- SQLite para desarrollo local
- PostgreSQL para producción
- Git
- GitHub
- Render
- Gunicorn
- WhiteNoise

---

## 📁 Estructura principal

```text
PROYECTO/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── static/
│   │   └── core/
│   │       └── styles.css
│   │
│   ├── templates/
│   │   └── core/
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore