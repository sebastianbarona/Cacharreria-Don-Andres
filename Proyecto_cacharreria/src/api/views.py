from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics
from rest_framework.views import APIView, Response, status
from .models import Productos, Usuarios,Categoria,Proveedor,Cliente,Venta,Credito
from .serializers import CategoriaSerializer,ProveedorSerializer,ClientesSerializer,VentaSerializer,CreditoSerializer,ProductosSerializer,UsuariosSerializer

  

#Login
class LoginView(APIView):
    
    def post(self, request):
        try:
            username = Usuarios.objects.get(username=request.username)
            password = Usuarios.objects.get(password=request.password) 

        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegistroUserView(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer



 #Usuarios
class UsuariosView(APIView):
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            usuarios_list = Usuarios.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(usuarios_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = UsuariosSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/usuarios/?page=' + str(nextPage), 'prevlink': '/api/usuarios/?page=' + str(previousPage)})


class UsuariosDetail(APIView):
#GET - Saber de un usuario
    def get(self,request, pk):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = UsuariosSerializer(usuario, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un usuario
    def put(self,request,pk):
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = UsuariosSerializer(usuario, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un usuario
    def delete(self,request,pk): 
        try:
            usuario = Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
 

class ProductosView(APIView):
    #Api productos
# GET - Devuelve todos los productos
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            producto_list = Productos.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(producto_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = ProductosSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/productos/?page=' + str(nextPage), 'prevlink': '/api/productos/?page=' + str(previousPage)})
# POST - Crea un nuevo producto    
    def post(self, request):
        if request.method == 'POST':
            serializer = ProductosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductosDetail(APIView):
#GET - Saber de un producto en especifico
    def get(self,request, pk):
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProductosSerializer(producto, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un producto
    def put(self,request,pk):
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = ProductosSerializer(producto, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un producto
    def delete(self,request,pk): 
        try:
            producto = Productos.objects.get(pk=pk)
        except Productos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class ProductosCompra(generics.ListAPIView):

    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            productoscompra = Productos.objects.filter(estado="Compra")
            page = request.GET.get('page',1)
            paginator = Paginator(productoscompra,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
            serializer = ProductosSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/productosCompra/?page=' + str(nextPage), 'prevlink': '/api/productosCompra/?page=' + str(previousPage)})
    
# ---------------------------------------- Categoria --------------------------

class CategoriasView(APIView):

# GET - Devuelve todos las categorias
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            categoria_list = Categoria.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(categoria_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = CategoriaSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/categorias/?page=' + str(nextPage), 'prevlink': '/api/categorias/?page=' + str(previousPage)})

# POST - Crea un nueva categoria    
    def post(self, request):
        if request.method == 'POST':
            serializer = CategoriaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoriasDetail(APIView):
#GET - Saber de una categoria en especifico
    def get(self,request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CategoriaSerializer(categoria, context={'request': request})
            return Response(serializer.data)

#PUT - Edita una categoria
    def put(self,request,pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = CategoriaSerializer(categoria, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina una categoria
    def delete(self,request,pk): 
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            categoria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------- Proveedor -----------------

class ProveedoresView(APIView):

# GET - Devuelve todos los proveedores
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            proveedor_list = Proveedor.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(proveedor_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = ProveedorSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/proveedor/?page=' + str(nextPage), 'prevlink': '/api/proveedor/?page=' + str(previousPage)})

# POST - Crear nuevo proveedor    
    def post(self, request):
        if request.method == 'POST':
            serializer = ProveedorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProveedoresDetail(APIView):
#GET - Saber de un proveedor especifico
    def get(self,request, pk):
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = Proveedor(proveedor, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un proveedor
    def put(self,request,pk):
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = ProveedorSerializer(proveedor, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un proveedor
    def delete(self,request,pk): 
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            proveedor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------- Cliente ----------------

class ClientesView(APIView):

# GET - Devuelve todos los clientes
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            clientes_list = Cliente.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(clientes_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = ClientesSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/clientes/?page=' + str(nextPage), 'prevlink': '/api/clientes/?page=' + str(previousPage)})

# POST - Crea un nuevo cliente 
    def post(self, request):
        if request.method == 'POST':
            serializer = ClientesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClientesDetail(APIView):
#GET - Saber de un cliente en especifico
    def get(self,request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ClientesSerializer(cliente, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un cliente
    def put(self,request,pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = ClientesSerializer(cliente, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un cliente
    def delete(self,request,pk): 
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            cliente.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------- Venta ---------------------

class VentasView(APIView):

# GET - Devuelve todos las ventas
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            ventas_list = Venta.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(ventas_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = VentaSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/ventas/?page=' + str(nextPage), 'prevlink': '/api/ventas/?page=' + str(previousPage)})

# POST - Crea un nueva venta    
    def post(self, request):
        if request.method == 'POST':
            serializer = VentaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VentasDetail(APIView):
#GET - Saber de una venta en especifico
    def get(self,request, pk):
        try:
            venta = Venta.objects.get(pk=pk)
        except Venta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = VentaSerializer(venta, context={'request': request})
            return Response(serializer.data)

#PUT - Edita una venta
    def put(self,request,pk):
        try:
            venta = Venta.objects.get(pk=pk)
        except Venta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = VentaSerializer(venta, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina una venta
    def delete(self,request,pk): 
        try:
            venta = venta.objects.get(pk=pk)
        except Venta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            venta.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


#---------------------------- Credito ------------

class CreditosView(APIView):

# GET - Devuelve todos las categorias
    def get(self, request, format=None):
        if request.method == 'GET':
            data = []
            nextPage = 1
            previousPage = 1
            creditos_list = Credito.objects.all()
            page = request.GET.get('page',1)
            paginator = Paginator(creditos_list,5)
            try:
                data = paginator.page(page)
            except PageNotAnInteger:
                data = paginator.page(1)
            except EmptyPage:
                data = paginator.page(paginator.num_pages)
                
            serializer = CreditoSerializer(data,context={'request': request} ,many=True)
            if data.has_next():
                nextPage = data.next_page_number()
            if data.has_previous():
                previousPage = data.previous_page_number()
                
            return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/creditos/?page=' + str(nextPage), 'prevlink': '/api/creditos/?page=' + str(previousPage)})

# POST - Crea un nuevo credito    
    def post(self, request):
        if request.method == 'POST':
            serializer = CreditoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreditosDetail(APIView):
#GET - Saber de un credito en especifico
    def get(self,request, pk):
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CreditoSerializer(credito, context={'request': request})
            return Response(serializer.data)

#PUT - Edita un credito
    def put(self,request,pk):
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = CreditoSerializer(credito, data=request.data,context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE - Elimina un credito
    def delete(self,request,pk): 
        try:
            credito = Credito.objects.get(pk=pk)
        except Credito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            credito.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
