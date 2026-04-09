# Testing Django CRUD App (Gestion-Productos)

## Setup

1. Navigate to the repo: `cd /home/ubuntu/repos/Gestion-Productos`
2. Start Django server: `python manage.py runserver 0.0.0.0:8000 &`
3. Verify server is running: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/` (expect 200)
4. Open in browser: `google-chrome http://127.0.0.1:8000/`

## Pages to Test

| Page | URL | What to verify |
|------|-----|----------------|
| List | `/` | Table with products, count chip, action buttons |
| Create | `/producto/crear/` | Form with fields: nombre, descripcion, precio, stock |
| Detail | `/producto/<id>/` | Detail rows, price, stock badge, action buttons |
| Edit | `/producto/<id>/editar/` | Pre-filled form, "Actualizar" button |
| Delete | `/producto/<id>/eliminar/` | Confirmation page with product info |
| Empty state | `/` (when no products) | Empty state icon, heading, CTA button |

## CRUD Test Flow

1. **CREATE**: Click "Nuevo Producto" → fill form → click "Guardar" → verify success alert and product in table
2. **READ (list)**: Verify table columns (ID, Nombre, Descripción, Precio, Stock, Acciones)
3. **READ (detail)**: Click eye icon → verify detail rows with labels and values
4. **UPDATE**: Click pencil icon or "Editar" → change stock to 0 → verify red "Sin stock" badge
5. **DELETE**: Click trash icon → verify confirmation page → click "Sí, eliminar" → verify product removed
6. **EMPTY STATE**: Delete all products → verify empty state with "No hay productos registrados"

## Key Visual Assertions

- Navbar: white background, indigo brand icon, indigo "Nuevo Producto" button
- Table headers: light gray, uppercase, small font
- Stock badges: green "X uds." for stock > 0, red "Sin stock" for stock = 0
- Prices: green colored text with $ prefix
- Action buttons: small squares with semantic colors (blue=view, amber=edit, red=delete)
- Alert dismiss: success alerts must have `.alert .alert-dismissible` classes for Bootstrap dismiss to work
- No text underlines on any `<a>` styled as button
- Footer: white with subtle top border

## Common Issues

- **Alert dismiss not working**: Ensure the alert div has Bootstrap's `.alert` and `.alert-dismissible` classes alongside custom classes. Without these, `data-bs-dismiss="alert"` won't function.
- **Font not loading**: "Plus Jakarta Sans" is loaded from Google Fonts CDN. If CDN is unavailable, fallback is `sans-serif`.
- **Translation popup in Chrome**: May appear when navigating Spanish-language pages. Close it before testing.

## No Devin Secrets Needed

This app runs locally with SQLite, no external credentials required.
