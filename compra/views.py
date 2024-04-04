from django.shortcuts import render , redirect
from . models import Producto , Proveedor 
from .forms import CrearProveedorForm , CrearProductoForm

# Create your views here.
def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mostrar_productos.html', {'productos': productos})

def mostrar_proveedores(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'mostrar_proveedores.html', {'proveedores': proveedor})


def crear_productos(request):
    if request.method == 'POST':
        form = CrearProductoForm(request.POST, request.FILES)  # Pass request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')  # Use the URL name instead of a hardcoded URL
    else:
        form = CrearProductoForm()

    return render(request, 'crear_productos.html', {'form': form})


def crear_proveedor(request):
    nuevo_proveedor = None  # Inicializamos la variable fuera del bloque condicional
    
    if request.method == 'POST':
        form = CrearProveedorForm(request.POST)
        if form.is_valid():
            nuevo_proveedor = form.save()
            # Redirigir a alguna página después de crear el proveedor
            return redirect('/mostar_proveedores.html')
    else:
        form = CrearProveedorForm()

    return render(request, 'crear_proveedor.html', {'form': form, 'proveedor': nuevo_proveedor})

#
def eliminar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('/mostar_proveedor.html')
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})