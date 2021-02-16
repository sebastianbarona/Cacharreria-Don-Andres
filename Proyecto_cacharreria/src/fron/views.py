from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from rest_framework.views import APIView, Response, status
from .forms import FormularioCLiente,FormularioCategoria,FormularioProveedor,FormularioProducto,FormularioVenta,FormularioCredito,FormularioUsuarios
from api.models import Categoria,Cliente,Credito,Productos,Proveedor,Usuarios,Venta
from api.serializers import CategoriaSerializer,ProveedorSerializer,ClientesSerializer,VentaSerializer,CreditoSerializer,ProductosSerializer,UsuariosSerializer
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
from reportlab.platypus import TableStyle,Table,SimpleDocTemplate,Spacer,Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm

# Create your views here.

def padre(request):

    return render(request,"padre.html")


def home(request):

    clientes=Cliente.objects.all
    productos=Productos.objects.all
    ventas=Venta.objects.all
    
    return render(request,"home.html",{"clientes":clientes,"productos":productos,"ventas":ventas})

#////////////////////////////////////////////////////////CLIENTE/////////////////////////////////////////////////////////////////////////

class FormularioCLienteView(HttpRequest):

    def cliente(request):
        
        clientes=Cliente.objects.all()

        return render(request,"cliente.html",{"clientes":clientes})


    def agregar_cliente(request):

        
        miformulario = FormularioCLiente()
        
        return render(request,"agregar_cliente.html",{"miformulario":miformulario})

    def procesar_cliente(request):

        miformulario = FormularioCLiente(request.POST)
        mensaje=("Cliente Registrado")
        
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioCLiente()
        return render(request,"agregar_cliente.html",{"miformulario":miformulario,"mensaje":mensaje})
        
    def modificar_cliente(request):

       shelf = Cliente.objects.all()

       upload = FormularioCLiente()
       if request.method == 'POST':
           upload = FormularioCLiente(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_cliente.html")           
            
       return render(request,"modificar_cliente.html",{"miformulario":upload,"shelf":shelf})

    def resultados_cliente(request,id_cliente):
            id_cliente= int (id_cliente)
            try:
                cliente_sel = Cliente.objects.get( id_cliente =  id_cliente)
            except  Cliente.DoesNotExist:
                return render(request, "resultados_cli.html")
            
            miformulario = FormularioCLiente(request.POST or None,instance= cliente_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioCLiente()
                mensaje=("Cliente Actualizado")
                return render(request,"resultados_cli.html",{"mensaje":mensaje})
            return render(request,"resultados_cli.html",{"miformulario":miformulario})


    def eliminar_cliente(request,id_cliente):
        id_cliente = int(id_cliente)
        try:
            cliente_sel = Cliente.objects.get(id_cliente = id_cliente)
        except Cliente.DoesNotExist:
             return render(request,"cliente.html")
        cliente_sel.delete()
        return render(request,"cliente.html")

#////////////////////////////////////////////////////////CATEGORIA/////////////////////////////////////////////////////////////////////////


class FormularioCategoriaView(HttpRequest):

    def categoria(request):

       shelf = Categoria.objects.all()

       upload = FormularioCategoria()
       if request.method == 'POST':
           upload = FormularioCategoria(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"categoria.html")           

       return render(request,"categoria.html",{"miformulario":upload,"shelf":shelf})


    def agregar_categoria(request):

        miformulario = FormularioCategoria()
        
        return render(request,"agregar_categoria.html",{"miformulario":miformulario})

    def procesar_categoria(request):

        miformulario = FormularioCategoria(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioCategoria()
        mensaje=("Categoria Registrada")
        return render(request,"agregar_categoria.html",{"miformulario":miformulario,"mensaje":mensaje})

    
    def modificar_categoria(request):

       shelf = Categoria.objects.all()

       upload = FormularioCategoria()
       if request.method == 'POST':
           upload = FormularioCategoria(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_categoria.html")           
            
       return render(request,"modificar_categoria.html",{"miformulario":upload,"shelf":shelf})

    def resultados_categoria(request,codigo_categoria):
            codigo_categoria= int (codigo_categoria)
            try:
                categoria_sel = Categoria.objects.get( codigo_categoria =  codigo_categoria)
            except  Categoria.DoesNotExist:
                return render(request, "resultados_cate.html")
            
            miformulario = FormularioCategoria(request.POST or None,instance= categoria_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioCategoria()
                mensaje=("Categoria Actualizada")
                return render(request,"resultados_cate.html",{"mensaje":mensaje})
            return render(request,"resultados_cate.html",{"miformulario":miformulario})


    def eliminar_categoria(request,codigo_categoria):
        codigo_categoria = int(codigo_categoria)
        try:
            categoria_sel = Categoria.objects.get(codigo_categoria = codigo_categoria)
        except Categoria.DoesNotExist:
             return render(request,"modificar_categoria.html")
        categoria_sel.delete()
        return render(request,"modificar_categoria.html")

#////////////////////////////////////////////////////////PROVEEDOR/////////////////////////////////////////////////////////////////////////


class FormularioProveedorView(HttpRequest):

    def proveedor(request):

        proveedores=Proveedor.objects.all()

        return render(request,"proveedor.html",{"proveedores":proveedores})


    def agregar_proveedor(request):

        miformulario = FormularioProveedor()
        
        return render(request,"agregar_proveedor.html",{"miformulario":miformulario})

    def procesar_proveedor(request):

        miformulario = FormularioProveedor(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioProveedor()
        mensaje=("Proveedor Registrado")
        return render(request,"agregar_proveedor.html",{"miformulario":miformulario,"mensaje":mensaje})

    
    def modificar_proveedor(request):

       shelf = Proveedor.objects.all()

       upload = FormularioProveedor()
       if request.method == 'POST':
           upload = FormularioProveedor(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_proveedor.html")           
            
       return render(request,"modificar_proveedor.html",{"miformulario":upload,"shelf":shelf})

    def resultados_proveedor(request,id_proveedor):
            id_proveedor= int (id_proveedor)
            try:
                proveedor_sel = Proveedor.objects.get( id_proveedor =  id_proveedor)
            except  Proveedor.DoesNotExist:
                return render(request, "resultados_proveedor.html")
            
            miformulario = FormularioProveedor(request.POST or None,instance= proveedor_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioProveedor()
                mensaje=("Proveedor Actualizado")
                return render(request,"resultados_proveedor.html",{"mensaje":mensaje})
            return render(request,"resultados_proveedor.html",{"miformulario":miformulario})


    def eliminar_proveedor(request,id_proveedor):
        id_proveedor = int(id_proveedor)
        try:
            proveedor_sel = Proveedor.objects.get(id_proveedor = id_proveedor)
        except Proveedor.DoesNotExist:
             return render(request,"proveedor.html")
        proveedor_sel.delete()
        return render(request,"proveedor.html")

#////////////////////////////////////////////////////////PRODUCTO/////////////////////////////////////////////////////////////////////////



class FormularioProductoView(HttpRequest):


    def producto(request):
    
        producto=Productos.objects.all()

        return render(request,"productos.html",{"productos":producto})

    def agregarproducto(request):

        miformulario = FormularioProducto()
        
        return render(request,"agregar_producto.html",{"miformulario":miformulario})


    def procesar_producto(request):

        miformulario = FormularioProducto(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioProducto()
        mensaje=("Producto Registrado")
        
        return render(request,"agregar_producto.html",{"miformulario":miformulario,"mensaje":mensaje})
        

    def modificar_producto(request):

       shelf = Productos.objects.all()

       upload = FormularioProducto()
       if request.method == 'POST':
           upload = FormularioProducto(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_producto.html")           
            
       return render(request,"modificar_producto.html",{"miformulario":upload,"shelf":shelf})


    def resultados_modi(request,id_producto):
            id_producto= int (id_producto)

            try:
                producto_sel = Productos.objects.get(id_producto = id_producto)
            except  Productos.DoesNotExist:
                return render(request, "resul_productomodi.html")
            
            miformulario = FormularioProducto(request.POST or None,instance= producto_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioProducto()
                mensaje=("Producto Actualizado")
                return render(request,"resul_productomodi.html",{"mensaje":mensaje})
            return render(request,"resul_productomodi.html",{"miformulario":miformulario})


    def eliminar_producto(request,id_producto):

        id_producto = int(id_producto)
        try:
            producto_sel = Productos.objects.get(id_producto = id_producto)
        except Productos.DoesNotExist:
             return render(request,"modificar_producto.html")
        producto_sel.delete()

        return render(request,"modificar_producto.html")


    def buscar(request):
    
        if request.GET["producto"]:

            producto=request.GET["producto"]
    
            articulo=Productos.objects.filter(nombre_producto__icontains=producto)

            return render(request,"resultados_pro.html",{"articulos":articulo,"query":producto})
    
        else:

            mensaje="No Hay Datos De Busqueda"    
     
        return HttpResponse(mensaje)        


#////////////////////////////////////////////////////////VENTAS/////////////////////////////////////////////////////////////////////////


class FormularioVentaView(HttpRequest):

    def venta(request):

        ventas=Venta.objects.all()
        creditos=Credito.objects.all()


        return render(request,"ventas.html",{"ventas":ventas,"creditos":creditos})

    def agregarventa(request):

        miformulario = FormularioVenta()
        
        return render(request,"agregar_venta.html",{"miformulario":miformulario})


    def procesar_venta(request):

        miformulario = FormularioVenta(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioVenta()
        mensaje=("Compra Registrada")
        return render(request,"agregar_venta.html",{"miformulario":miformulario,"mensaje":mensaje})

    def modifi_venta_general(request):

        return render(request,"modificargeneral.html")

    def modificar_venta(request):

       shelf = Venta.objects.all()

       upload = FormularioVenta()
       if request.method == 'POST':
           upload = FormularioVenta(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_venta.html")           
            
       return render(request,"modificar_venta.html",{"miformulario":upload,"shelf":shelf})


    def resultados_venta(request,id_venta):
            id_venta= int (id_venta)

            try:
                venta_sel = Venta.objects.get(id_venta = id_venta)
            except  Venta.DoesNotExist:
                return render(request, "resultados_venta.html")
            
            miformulario = FormularioVenta(request.POST or None,instance= venta_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioVenta()
                mensaje=("Venta Actualizado")
                return render(request,"resultados_venta.html",{"mensaje":mensaje})
            return render(request,"resultados_venta.html",{"miformulario":miformulario})

    def eliminar_venta(request,id_venta):

        id_venta = int(id_venta)
        try:
            venta_sel = Venta.objects.get(id_venta = id_venta)
        except Venta.DoesNotExist:
             return render(request,"ventas.html")
        venta_sel.delete()
        return render(request,"ventas.html")

#////////////////////////////////////////////////////////CREDITO/////////////////////////////////////////////////////////////////////////

class FormularioCreditoView(HttpRequest):

    def agregarcredito(request):

        miformulario = FormularioCredito()        

        return render(request,"agregar_credito.html",{"miformulario":miformulario})


    def procesar_credito(request):

        miformulario = FormularioCredito(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioCredito()
        mensaje=("Compra Registrada")
        return render(request,"agregar_credito.html",{"miformulario":miformulario,"mensaje":mensaje})

    def modificar_credito(request):

       shelf = Credito.objects.all()

       upload = FormularioCredito()
       if request.method == 'POST':
           upload = FormularioCredito(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_credito.html")           
            
       return render(request,"modificar_credito.html",{"miformulario":upload,"shelf":shelf})


    def resultados_credito(request,id_credito):
            id_credito= int (id_credito)

            try:
                credito_sel = Credito.objects.get(id_credito = id_credito)
            except  Credito.DoesNotExist:
                return render(request, "resultados_cred.html")
            
            miformulario = FormularioCredito(request.POST or None,instance= credito_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioCredito()
                mensaje=("Credito Actualizado")
                return render(request,"resultados_cred.html",{"mensaje":mensaje})
            return render(request,"resultados_cred.html",{"miformulario":miformulario})


    def eliminar_credito(request,id_credito):
        id_credito = int(id_credito)
        try:
            credito_sel = Credito.objects.get(id_credito = id_credito)
        except Credito.DoesNotExist:
             return render(request,"credito.html")
        credito_sel.delete()

        return render(request,"credito.html")

#////////////////////////////////////////////////////////USUARIO/////////////////////////////////////////////////////////////////////////
class FormularioUsuariosView(HttpRequest):


    def usuarios(request):
    
        usuarios=Usuarios.objects.all()

        return render(request,"Usuarios.html",{"usuarios":usuarios})


    def agregarusuario(request):

        miformulario = FormularioUsuarios()        

        return render(request,"agregar_usuario.html",{"miformulario":miformulario})


    def procesar_usuario(request):

        miformulario = FormularioUsuarios(request.POST)
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioUsuarios()
        mensaje=("Usuario Registrado")
        return render(request,"agregar_usuario.html",{"miformulario":miformulario,"mensaje":mensaje})

    def modificar_usuario(request):

       shelf = Usuarios.objects.all()

       upload = FormularioUsuarios()
       if request.method == 'POST':
           upload = FormularioUsuarios(request.POST)
           if upload.is_valid():
               upload.save
               return render(request,"modificar_usuario.html")           
            
       return render(request,"modificar_usuario.html",{"miformulario":upload,"shelf":shelf})


    def resultados_usuario(request,id_persona):
            id_persona= int (id_persona)

            try:
                usuario_sel = Usuarios.objects.get(id_persona = id_persona)
            except  Usuarios.DoesNotExist:
                return render(request, "resultados_usua.html")
            
            miformulario = FormularioUsuarios(request.POST or None,instance= usuario_sel)            
            if miformulario.is_valid():
                miformulario.save()
                miformulario = FormularioUsuarios()
                mensaje=("Credito Actualizado")
                return render(request,"resultados_usua.html",{"mensaje":mensaje})
            return render(request,"resultados_usua.html",{"miformulario":miformulario})


    def eliminar_usuario(request,id_usuario):
        id_persona = int(id_persona)
        try:
            usuario_sel = Usuarios.objects.get(id_persona = id_persona)
        except Usuarios.DoesNotExist:
             return render(request,"resultados_usua.html")
        usuario_sel.delete()

        return render(request,"resultados_usua.html")


#////////////////////////////////////////////////////////LOGIN/////////////////////////////////////////////////////////////////////////

def login(request):
    

   shelf = Usuarios.objects.all()

   upload = FormularioUsuarios()
   if request.method == 'POST':
       upload = FormularioUsuarios(request.POST)
       if upload.is_valid():
           upload.save
           return render(request,"logueo.html")           
            
   return render(request,"logueo.html",{"miformulario":upload,"shelf":shelf})


def verificacion(request,id_persona):
        id_persona= int (id_persona)
        try:
            usuario_sel = Usuarios.objects.get(id_persona = id_persona)

        except  Usuarios.DoesNotExist:
            return render(request, "loguin.html")
            
        miformulario = FormularioUsuarios(request.POST or None,instance= usuario_sel)            
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioUsuarios()
            mensaje=("Usuario Actualizado")
            return render(request,"home.html",{"mensaje":mensaje})
        return render(request,"home.html")

#////////////////////////////////////////////////////////Report/////////////////////////////////////////////////////////////////////////


class ReporteVenta(object):

    def __init__(self):
        self.buf = BytesIO()

    def run(self):
        self.doc = SimpleDocTemplate(self.buf)
        self.story = []
        self.encabezado()
        self.crearTabla()
        self.encabezado2()
        self.crearTabla2()
        self.doc.build(self.story, onFirstPage=self.numeroPagina, 
            onLaterPages=self.numeroPagina)
        pdf = self.buf.getvalue()
        self.buf.close()
        return pdf

    def encabezado(self):
        p = Paragraph("Reporte Ventas", self.estiloPC())
        self.story.append(p)
        self.story.append(Spacer(1,0.5*inch))

    def encabezado2(self):
        self.story.append(Spacer(1,0.5*inch))
        p = Paragraph("Reporte Credito", self.estiloPC())
        self.story.append(p)
        self.story.append(Spacer(1,0.5*inch))

    def crearTabla(self):

        data = [["Producto","Cliente","Empleado","Monto"]] \
            +[[x.id_producto, x.id_cliente, x.id_usuario, x.monto_venta] 
                for x in Venta.objects.all() ]
                            
        style = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE')])

        t = Table(data)
        t.setStyle(style)
        self.story.append(t)
    
    def crearTabla2(self):
                            
        data2 = [["Producto","Cliente","Saldo"]] \
            +[[x.id_producto, x.id_cliente, x.saldo_pendiente] 
                for x in Credito.objects.all()]
                

        style = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE')])


        t2 = Table(data2)
        t2.setStyle(style)
        self.story.append(t2)

    def estiloPC(self):
        return ParagraphStyle(name="centrado", alignment=TA_CENTER)

    def numeroPagina(self,canvas,doc):
        num = canvas.getPageNumber()
        text = "Pagina %s" % num
        canvas.drawRightString(200*mm, 20*mm, text)

    def reporte_ventas(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ventas.pdf"'
        r = ReporteVenta()
        response.write(r.run())
        return response
