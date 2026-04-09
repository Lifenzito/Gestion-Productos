# Taller 2 — CRUD con Django MVT

## Descripción
Aplicación web en Python con Django que implementa un CRUD completo para el modelo **Producto**, siguiendo la arquitectura Model-View-Template (MVT).

---

## Estructura del proyecto

```
crud_productos/
├── manage.py
├── crud_productos/          ← Configuración del proyecto
│   ├── settings.py
│   └── urls.py
└── productos/               ← Aplicación principal
    ├── models.py            ← M: Modelo de datos (Producto)
    ├── views.py             ← V: Lógica de las vistas CRUD
    ├── forms.py             ← Formulario Django
    ├── urls.py              ← Enrutamiento de URLs
    ├── admin.py             ← Panel de administración
    └── templates/
        └── productos/
            ├── base.html              ← Template base con Bootstrap
            ├── lista.html             ← READ: Lista de productos
            ├── detalle.html           ← READ: Detalle de un producto
            ├── formulario.html        ← CREATE / UPDATE
            └── confirmar_eliminar.html ← DELETE: Confirmación
```

---

## Instalación y ejecución

### 1. Requisitos
```bash
pip install django
```

### 2. Ir a la carpeta del proyecto
```bash
cd crud_productos
```

### 3. Crear la base de datos (migraciones)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. (Opcional) Crear superusuario para el admin
```bash
python manage.py createsuperuser
```

### 5. Correr el servidor
```bash
python manage.py runserver
```

### 6. Abrir en el navegador
- **App principal:** http://127.0.0.1:8000/
- **Panel admin:** http://127.0.0.1:8000/admin/

---

## Rutas disponibles

| URL | Vista | Operación |
|-----|-------|-----------|
| `/` | lista_productos | READ — Lista todos los productos |
| `/producto/<id>/` | detalle_producto | READ — Detalle de un producto |
| `/producto/crear/` | crear_producto | CREATE — Formulario de creación |
| `/producto/<id>/editar/` | editar_producto | UPDATE — Formulario de edición |
| `/producto/<id>/eliminar/` | eliminar_producto | DELETE — Confirmación y eliminación |

---

## Modelo de datos

**Producto**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| nombre | CharField | Nombre del producto (max 200 chars) |
| descripcion | TextField | Descripción larga |
| precio | DecimalField | Precio con 2 decimales |
| stock | PositiveIntegerField | Cantidad disponible |
| fecha_creacion | DateTimeField | Fecha automática de creación |
