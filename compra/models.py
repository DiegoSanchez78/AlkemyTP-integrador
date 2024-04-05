from django.db import models

# Create your models here.
class Proveedor(models.Model):
    # empresa = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    # cuit = models.IntegerField()

    def __str__(self):
        return f'{ self.nombre} {self.apellido}'

    
    class Meta:
        verbose_name = "Proveedor"
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    stock_actual = models.IntegerField()
    # detalles = models.TextField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE )
    def __str__(self):
        return f'Producto {self.nombre}-{self.imagen}'
    class Meta:
        verbose_name = "Producto"
