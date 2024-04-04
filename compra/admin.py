from django.contrib import admin
from .models import Proveedor , Producto

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'dni')
    list_display_links = ('nombre' , 'apellido' , 'dni')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre' , 'proveedor' , 'stock_actual', 'imagen', 'precio')
    list_display_links = ('nombre' , 'proveedor')

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Producto, ProductoAdmin)