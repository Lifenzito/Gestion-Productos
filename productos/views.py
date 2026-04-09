from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


# READ - Listar todos los productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})


# READ - Ver detalle de un producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})


# CREATE - Crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" creado exitosamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario.html', {
        'form': form,
        'titulo': 'Crear Producto',
        'accion': 'Guardar'
    })


# UPDATE - Editar un producto existente
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado correctamente.')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/formulario.html', {
        'form': form,
        'titulo': f'Editar: {producto.nombre}',
        'accion': 'Actualizar',
        'producto': producto
    })


# DELETE - Eliminar un producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado correctamente.')
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminar.html', {'producto': producto})
