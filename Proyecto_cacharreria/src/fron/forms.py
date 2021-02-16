from django import forms
from django.forms import ModelForm ,CharField,PasswordInput
from api.models import Categoria,Cliente,Credito,Productos,Proveedor,Usuarios,Venta
from django.contrib.auth.forms import UserCreationForm



class FormularioCLiente(forms.ModelForm):

 class Meta:
  
      model = Cliente
      fields = '__all__'
#----------------------------------------------------------------------------------------------------------
      
class FormularioCategoria(forms.ModelForm):

 class Meta:
  
      model = Categoria
      fields = '__all__'

#----------------------------------------------------------------------------------------------------------
class FormularioProveedor(forms.ModelForm):

 class Meta:

  
      model = Proveedor
      fields = '__all__'

#----------------------------------------------------------------------------------------------------------
 

class FormularioProducto(forms.ModelForm):


  class Meta:

  
      model = Productos
      fields =('imagen_producto','id_producto','nombre_producto','codigo','id_proveedor','estado_producto','cantidad_producto','precio_producto','imagen_producto')
     

#----------------------------------------------------------------------------------------------------------

class FormularioVenta(forms.ModelForm):

 class Meta:

  
      model = Venta
      fields = '__all__'

#----------------------------------------------------------------------------------------------------------

class FormularioCredito(forms.ModelForm):

 class Meta:

  
      model = Credito
      fields = '__all__'

class FormularioUsuarios(forms.ModelForm):

  class Meta:

      model = Usuarios

      password = forms.CharField(widget=forms.PasswordInput)
      password2 = forms.CharField(widget=forms.PasswordInput)
      fields= '__all__'
   

   