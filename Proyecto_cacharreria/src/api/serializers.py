from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator 
from django.contrib.auth.password_validation import validate_password
from .models import Productos, Usuarios,Cliente,Categoria,Proveedor,Venta,Credito



    
class UsuariosSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=Usuarios.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = Usuarios
        fields = ('id_persona','username','email','nombre_persona','password','password2','rol_usuario')
        extra_kwargs = {
            'nombre_persona': {'required': True},
            'rol_usuario': {'required': True}
        }

    def validate(self, attes):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords no coinciden."})

        return attrs

    def create(self, validated_data):
        user = Usuarios.objects.create(
            id_persona= validated_data['id_persona'],
            username= validated_data['username'],
            email = validated_data['email'],
            nombre_persona=validated_data['nombre_persona'],
            rol_usuario=validated_data['lastname']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('pk','id_categoria','nombre_categoria','codigo_categoria')

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('pk''id_proveedor','nombre_proveedor','cantidad_articulos','precio_producto')

class ProductosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productos
        fields = ('pk','id_producto','nombre_producto',
                'codigo','id_proveedor','estado_producto',
                'cantidad_producto','precio_producto','imagen_producto')

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ('pk','id_cliente','nombre_cliente','cedula_cliente',
                'estado_cliente','telefono_cliente')

class VentaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Venta
        fields = ('pk',' id_venta','id_producto','id_cliente','id_usuario','monto_venta')

class CreditoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = ('pk','id_producto','id_cliente','saldo_pendiente')
