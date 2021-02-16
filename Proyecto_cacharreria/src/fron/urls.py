
from django.urls import path
from fron.views import home,login,padre,FormularioCLienteView,FormularioCategoriaView
from fron.views import FormularioProductoView,FormularioVentaView,FormularioCLienteView,ReporteVenta
from fron.views import FormularioProveedorView,FormularioCreditoView,FormularioUsuariosView,verificacion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',login,name="Login"),
    path('verificacion/<str:id_persona>',verificacion,name="Verificacion"),
    path('home',home,name="Home"),
    path('padre',padre,name="Padre"),

    path('cliente',FormularioCLienteView.cliente,name="Cliente"),
    path('agregarcliente',FormularioCLienteView.agregar_cliente,name="AGRcliente"),
    path('procesar_cliente',FormularioCLienteView.procesar_cliente,name="PRcliente"),
    path('modicliente',FormularioCLienteView.modificar_cliente,name="MODcliente"),
    path('eliminarcliente/<int:id_cliente>',FormularioCLienteView.eliminar_cliente,name="ELIcliente"),
    path('resulmodicliente/<int:id_cliente>',FormularioCLienteView.resultados_cliente),
    

    path('proveedor',FormularioProveedorView.proveedor,name="Proveedor"),
    path('agregarproveedor',FormularioProveedorView.agregar_proveedor,name="AGRproveedor"),
    path('procesar_proveedor',FormularioProveedorView.procesar_proveedor,name="PRproveedor"),
    path('modiproveedor',FormularioProveedorView.modificar_proveedor,name="MODproveedor"),
    path('eliminarproveedor/<int:id_proveedor>',FormularioProveedorView.eliminar_proveedor,name="ELIproveedor"),
    path('resulmodiproveedor/<int:id_proveedor>',FormularioProveedorView.resultados_proveedor),
    

    path('categoria',FormularioCategoriaView.categoria ,name="Categoria"),
    path('agregar_categoria',FormularioCategoriaView.agregar_categoria ,name="AGRcategoria"),
    path('procesar_categoria',FormularioCategoriaView.procesar_categoria, name="PRcategoria"),
    path('modicategoria',FormularioCategoriaView.modificar_categoria, name="MODcategoria"),
    path('resulmodicategoria/<int:codigo_categoria>',FormularioCategoriaView.resultados_categoria),
    path('eliminarcategoria/<int:codigo_categoria>',FormularioCategoriaView.eliminar_categoria, name="ELIcategoria"),
    

    path('Producto',FormularioProductoView.producto,name="Producto"),
    path('agregarproducto',FormularioProductoView.agregarproducto,name="AGRproducto"), 
    path('procesar_producto',FormularioProductoView.procesar_producto,name="PRproducto"),
    path('modiproducto',FormularioProductoView.modificar_producto,name="MODproducto"),
    path('resulmodipro/<int:id_producto>',FormularioProductoView.resultados_modi),
    path('eliminarproducto/<int:id_producto>',FormularioProductoView.eliminar_producto,name="ELIproducto"),
    path('buscar/',FormularioProductoView.buscar,name="Buscar"),
    

    path('venta',FormularioVentaView.venta,name="Venta"),    
    path('agregarventa',FormularioVentaView.agregarventa,name="AGRventa"),
    path('procesar_venta',FormularioVentaView.procesar_venta,name="PRventa"),
    path('modigeneral',FormularioVentaView.modifi_venta_general,name="MODventageneral"),  
    path('modiventa',FormularioVentaView.modificar_venta,name="MODventa"),
    path('resulmodiventa/<int:id_venta>',FormularioVentaView.resultados_venta),
    path('eliminarventa/<int:id_venta>',FormularioVentaView.eliminar_venta,name="ELIventa"),
    path('reporte_ventas',ReporteVenta.reporte_ventas,name="reporte_ventas_pdf"),
   

    path('agregarcredito',FormularioCreditoView.agregarcredito, name="AGRcredito"),
    path('procesar_credito',FormularioCreditoView.procesar_credito, name="PRcredito"),
    path('modicredito',FormularioCreditoView.modificar_credito, name="MODcredito"),
    path('resulmodicredito/<int:id_credito>',FormularioCreditoView.resultados_credito),
    path('eliminarcredito/<int:id_credito>',FormularioCreditoView.eliminar_credito, name="ELIcredito"),
    
    path('usuario',FormularioUsuariosView.usuarios,name="Usuario"),
    path('agregarusuario',FormularioUsuariosView.agregarusuario,name="AGRusuario"),
    path('procesar_usuario',FormularioUsuariosView.procesar_usuario,name="PRusuario"),
    path('modiusuario',FormularioUsuariosView.modificar_usuario,name="MODusuario"),
    path('eliminarusuario/<int:id_persona>',FormularioUsuariosView.eliminar_usuario,name="ELIusuario"),
    path('resulmodiusuario/<int:id_persona>',FormularioUsuariosView.resultados_usuario),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)