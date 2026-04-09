# Testing Gestion-Productos Django CRUD App

## Environment Setup

1. Start Django dev server:
   ```bash
   cd /home/ubuntu/repos/Gestion-Productos
   python manage.py runserver 0.0.0.0:8000 &
   ```
2. Verify server is running: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/`

## Chrome Launch

The `google-chrome` wrapper at `~/.local/bin/google-chrome` is a CDP proxy script that expects Chrome already running on port 29229. To launch Chrome from scratch:

```bash
DISPLAY=:0 /opt/.devin/chrome/chrome/linux-133.0.6943.126/chrome-linux64/chrome \
  --remote-debugging-port=29229 \
  --no-first-run --no-default-browser-check \
  --disable-session-crashed-bubble --disable-infobars \
  http://127.0.0.1:8000/ &
```

Note: The Chrome binary path might change across environments. If the path above doesn't work, search for Chrome with:
```bash
find /opt/.devin/chrome -name "chrome" -type f
```

After launch, maximize with:
```bash
DISPLAY=:0 wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
```

## Testing the CRUD Flow

The app has 5 pages to test:
1. **List page** (`/`) - Shows product table with action buttons
2. **Create form** (`/producto/crear/`) - Form with Nombre, Descripcion, Precio, Stock fields
3. **Detail page** (`/producto/<id>/`) - Shows product details in row layout
4. **Edit form** (`/producto/<id>/editar/`) - Pre-filled form for editing
5. **Delete confirmation** (`/producto/<id>/eliminar/`) - Confirmation page with warning

### Key Visual Elements to Verify
- Navbar: dark gradient background with brand text and green pill "Nuevo Producto" button
- Table: gradient header with uppercase labels, action buttons (blue eye, orange pencil, red trash)
- Stock badges: green gradient for stock > 0, red gradient "Sin stock" for stock = 0
- Price: green gradient text with `$` prefix
- Cards: rounded corners (20px), shadow, dark gradient headers
- Buttons: NO text underline on any `<a>` styled as button (text-decoration: none)
- Footer: dark gradient with branding
- Empty state: purple gradient inbox icon, "No hay productos registrados", "Crear el primero" CTA

### Recommended Test Flow
1. Verify list page styling with existing product
2. Create new product and verify success alert + green stock badge
3. View product detail and verify layout/styling
4. Edit product (change stock to 0) and verify red "Sin stock" badge
5. Delete product and verify confirmation page styling
6. Verify empty state when no products exist
7. Restore original product data

## Database
- SQLite at `db.sqlite3`
- Model: `Producto` with fields: nombre, descripcion, precio, stock, fecha_creacion
- Django admin is not configured; manage data through the CRUD UI or `python manage.py shell`

## Notes
- No CI is configured in this repo
- The app uses Bootstrap 5.3.0 + custom CSS with gradients and animations
- Google Font "Inter" is loaded from CDN
- All CSS is inline in `base.html` (no separate CSS files)
- Language is Spanish (es-co), timezone America/Bogota
