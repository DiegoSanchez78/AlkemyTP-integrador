from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_productos, name='mostrar_productos'),
    path('crear_productos/', views.crear_productos, name='crear_productos'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/', views.mostrar_proveedores, name='proveedor'),
    path('mostrar_productos', views.mostrar_productos, name='mostar_productos'),
]