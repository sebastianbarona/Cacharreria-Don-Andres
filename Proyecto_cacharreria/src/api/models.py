from django.db import models
from django.contrib.auth.models import User

#Manager Models
from api.managers import ProveedorManager

#Usuarios
class Usuarios(models.Model):

    Status=((('A','Admin')),(('O','Operador')),)

    id_persona = models.AutoField(primary_key= True)
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    nombre_persona = models.CharField('Nombre', max_length=100)   
    password = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    rol_usuario = models.CharField(

        max_length=32,choices=Status,default='available',
    )
    createdAt = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["id_persona"]


    def __str__(self):
        return self.nombre_persona

#Categoria
class Categoria(models.Model):
    id_categoria = models.CharField(max_length=20)
    nombre_categoria = models.CharField(max_length=20)
    codigo_categoria = models.CharField(primary_key=True,max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ["codigo_categoria"]

    #Metodos
    def __str__(self):
        return self.nombre_categoria


#Proveedor
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    cantidad_articulos = models.IntegerField()
    precio_producto = models.IntegerField() 
    createdAt = models.DateTimeField(auto_now_add=True)

    objects = ProveedorManager()
    
    class Meta:
        ordering = ["id_proveedor"]

    #Metodos
    def __str__(self):
        return self.nombre_proveedor


#Producto
class Productos(models.Model):
    #Crear el modelo para los productos
    Status=((('Compra','Compra Producto')),(('Venta','Venta Producto')),(('Pendiente',' Pendiente Producto')),)

    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    codigo =  models.ForeignKey(Categoria,on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    estado_producto = models.CharField(

        max_length=32,choices=Status,default='available',
    )
    cantidad_producto = models.IntegerField()
    precio_producto = models.IntegerField()
    imagen_producto = models.URLField(max_length=400)
    createdAt = models.DateTimeField(auto_now_add=True)

    #Metada
    class Meta:
        ordering = ["id_producto"]

    #Metodos
    def __str__(self):
        return self.nombre_producto


#Cliente
class Cliente(models.Model):

    Status=((('Nuevo','Cliente Nuevo')),(('Antiguo','CLiente Antiguo')),)

    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100,null=False)
    cedula_cliente = models.CharField(unique=True,max_length=100,null=False)
    estado_cliente =  models.CharField(

        max_length=32,choices=Status,default='available',
    )
    telefono_cliente = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)


 #Metada
    class Meta:
        ordering = ["id_cliente"]
    
    def __str__(self):
        return self.nombre_cliente

#Venta
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    monto_venta = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)


    #Metada
    class Meta:
        ordering = ["id_venta"]

    def __str__(self):
        return self.id_cliente.nombre_cliente

    
#Credito
class Credito(models.Model):
    id_credito = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    saldo_pendiente = models.IntegerField() 
    createdAt = models.DateTimeField(auto_now_add=True)


     #Metada
    class Meta:
        ordering = ["id_cliente"]

    def __str__(self):
        return self.id_cliente




