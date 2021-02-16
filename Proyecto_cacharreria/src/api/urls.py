from django.urls import path, include
from api import views

#from api.views import Login,Logout

#Views




urlpatterns = [
    path('registro/', views.RegistroUserView.as_view()),
    path('usuarios/', views.UsuariosView.as_view()),
    path('usuariosDetail/<int:pk>',views.UsuariosDetail.as_view()),    
    path('productos/', views.ProductosView.as_view()),
    path('productosDetail/<int:pk>', views.ProductosDetail.as_view()),
    path('productosCompra/', views.ProductosCompra.as_view(), name='Compra'),
    path('categorias/', views.CategoriasView.as_view()),
    path('categoriasDetail/<int:pk>', views.CategoriasDetail.as_view()),
    path('proveedores/', views.ProveedoresView.as_view()),
    path('proveedoresDetail/<int:pk>', views.ProveedoresDetail.as_view()),
    path('clientes/', views.ClientesView.as_view()),
    path('clientesDetail/<int:pk>', views.ClientesDetail.as_view()),
    path('ventas/', views.VentasView.as_view()),
    path('ventasDetail/<int:pk>', views.VentasDetail.as_view()),
    path('credito/', views.CreditosView.as_view()),
    path('creditoDetail/<int:pk>', views.CreditosDetail.as_view()),
    #path('', include(router.urls))
]