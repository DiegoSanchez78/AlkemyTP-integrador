from django.urls import path
from . import views


urlpatterns = [
    path('', views.mostrar_productos, name='mostrar_productos'),
    path('crear_productos/', views.crear_productos, name='crear_productos'),
    path('crear_proveedor/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/', views.mostrar_proveedores, name='proveedor'),
    path('mostrar_productos', views.mostrar_productos, name='mostar_productos'),
]


urlpatterns += [
    path('actualizar_producto/<int:pk>/', views.ProductoUpdateView.as_view(), name='update'),
    path('eliminar_producto/<int:pk>/', views.ProductoDeleteView.as_view(), name='delete'),
    path('detalle_producto/<int:pk>/', views.ProductoDetailView.as_view(), name='detail'),
    path('detalle_proveedor/<int:pk>/', views.ProveedorDetailView.as_view(), name='detail_proveedor'),
    path('actualizar_proveedores/<int:pk>/', views.ProveedorUpdateView.as_view(), name='update_proveedores'),
    path('eliminar_proveedor/<int:pk>/', views.ProveedorDeleteView.as_view(), name='delete_proveedor'),

]