from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.Usuarios)
admin.site.register(models.Productos)
admin.site.register(models.Proveedor)
admin.site.register(models.Categoria)
admin.site.register(models.Cliente)
admin.site.register(models.Credito)
admin.site.register(models.Venta)

