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
- Solo el autor puede editar o eliminar su propia publicación

### Productos

- Listado de productos
- Búsqueda de productos por nombre
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

El formulario de contacto incluye una validación personalizada para comprobar la longitud mínima del mensaje.

### Administración

La aplicación utiliza Django Admin para administrar:

- Usuarios
- Grupos
- Permisos
- Productos
- Perfiles
- Publicaciones

---

## 🔐 Permisos y seguridad

Se implementaron diferentes niveles de acceso según el usuario.

Los productos utilizan el sistema de permisos incorporado en Django para controlar las acciones de creación, edición y eliminación.

En el blog:

- Cualquier usuario puede visualizar las publicaciones.
- Es necesario iniciar sesión para crear una publicación.
- El autor se asigna automáticamente al usuario autenticado.
- Cada usuario puede editar únicamente sus propias publicaciones.
- Cada usuario puede eliminar únicamente sus propias publicaciones.

La aplicación también utiliza variables de entorno para evitar almacenar información sensible directamente en el repositorio.

---

## 🎨 Diseño

La aplicación utiliza HTML y CSS personalizado.

Incluye:

- Diseño responsive
- Barra de navegación
- Cards para productos y funcionalidades
- Formularios estilizados
- Página de inicio personalizada
- Diseño específico para productos
- Diseño específico para publicaciones
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
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
│   ├── migrations/
│   │
│   ├── static/
│   │   └── core/
│   │       └── styles.css
│   │
│   ├── templates/
│   │   └── core/
│   │       ├── acerca_de.html
│   │       ├── base.html
│   │       ├── contacto.html
│   │       ├── crear_producto.html
│   │       ├── crear_publicacion.html
│   │       ├── detalle_publicacion.html
│   │       ├── editar_producto.html
│   │       ├── editar_publicacion.html
│   │       ├── eliminar_producto.html
│   │       ├── eliminar_publicacion.html
│   │       ├── inicio.html
│   │       ├── login.html
│   │       ├── perfil.html
│   │       ├── productos.html
│   │       ├── publicaciones.html
│   │       └── registro.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 💻 Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/renzobarbonii-cyber/proyecto-django-coderhouse.git
```

### 2. Entrar al proyecto

```bash
cd proyecto-django-coderhouse
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

### 7. Crear un superusuario

Este paso es opcional, pero permite acceder al panel administrativo de Django.

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el servidor

```bash
python manage.py runserver
```

La aplicación estará disponible localmente en:

```text
http://127.0.0.1:8000/
```

El panel administrativo estará disponible en:

```text
http://127.0.0.1:8000/admin/
```

---

## 🌍 Despliegue

La aplicación se encuentra desplegada mediante Render.

En producción utiliza:

- PostgreSQL como base de datos
- Gunicorn como servidor WSGI
- WhiteNoise para servir archivos estáticos
- Variables de entorno para información sensible
- Migraciones automáticas durante el proceso de despliegue
- Recolección de archivos estáticos mediante `collectstatic`

La aplicación pública está disponible en:

https://proyecto-django-coderhouse.onrender.com

---

## 🔑 Variables de entorno

Para producción se utilizan variables de entorno como:

```text
DATABASE_URL
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
```

Estas variables permiten mantener fuera del repositorio información sensible como la clave secreta de Django y las credenciales de la base de datos.

---

## 🗄️ Base de datos

Durante el desarrollo local, el proyecto utiliza SQLite.

En producción, la aplicación utiliza PostgreSQL mediante Render.

Esto permite mantener los datos almacenados de forma independiente al servidor web desplegado.

---

## 📚 Conceptos aplicados

El proyecto integra los principales conceptos trabajados durante el curso de Python y Django:

- Modelos
- Migraciones
- Bases de datos
- CRUD
- Django Admin
- Django Forms
- ModelForms
- Templates
- Herencia de templates
- URLs nombradas
- Namespaces
- Function Based Views
- Class Based Views
- Autenticación
- Registro de usuarios
- Perfiles de usuario
- Permisos
- Relaciones entre modelos
- Validaciones
- Archivos estáticos
- Git
- GitHub
- Despliegue de una aplicación web

---

## 🎯 Objetivo del proyecto

El objetivo del proyecto es integrar en una aplicación web funcional los conocimientos adquiridos durante el curso.

La aplicación demuestra el uso de Django para desarrollar un sistema que permite gestionar información, autenticar usuarios, controlar permisos, trabajar con formularios, implementar un blog y desplegar el resultado mediante una URL pública.

---

## 👨‍💻 Autor

Proyecto desarrollado por Renzo Barboni como parte del curso de Python y Django de Coderhouse.