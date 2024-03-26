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
    nuevo_producto = None 
    if request.method == 'POST':
        form = CrearProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save()
            # Redirigir a alguna página después de crear el proveedor
            return redirect('/mostar_productos.html')
    else:
        form = CrearProductoForm()

    return render(request, 'crear_productos.html', {'form': form, 'productos': nuevo_producto})

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