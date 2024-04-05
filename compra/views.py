from django.shortcuts import render , redirect
from . models import Producto , Proveedor 
from .forms import CrearProveedorForm , CrearProductoForm
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mostrar_productos.html', {'productos': productos})

def mostrar_proveedores(request):
    proveedor = Proveedor.objects.all()
    return render(request, 'mostrar_proveedores.html', {'proveedores': proveedor})


def crear_productos(request):
    if request.method == 'POST':
        form = CrearProductoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')  
    else:
        form = CrearProductoForm()

    return render(request, 'crear_productos.html', {'form': form})


def crear_proveedor(request):
    nuevo_proveedor = None 
    
    if request.method == 'POST':
        form = CrearProveedorForm(request.POST)
        if form.is_valid():
            nuevo_proveedor = form.save()
            return redirect('proveedor')
    else:
        form = CrearProveedorForm()

    return render(request, 'crear_proveedor.html', {'form': form, 'proveedor': nuevo_proveedor})



from django.urls import reverse_lazy
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'  
    success_url = reverse_lazy('mostrar_productos')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'actualizar_producto.html'
    fields = ['nombre', 'precio', 'imagen', 'stock_actual', 'proveedor']  
    success_url = reverse_lazy('mostrar_productos')  
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'detalle_proveedor.html'
    

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'actualizar_proveedor.html'
    fields = ['nombre', 'apellido', 'dni']
    success_url = reverse_lazy('proveedor')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'eliminar_proveedor.html'
    success_url = reverse_lazy('proveedor')