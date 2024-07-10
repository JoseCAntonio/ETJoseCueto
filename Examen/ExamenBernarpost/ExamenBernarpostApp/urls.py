from django.urls import path
from . import views


urlpatterns = [
    path('Adminn/', views.home , name='admin'),
    path('registrarUsuario/',views.registrarUsuario,name='registrarUsuario'),
    path('registrarPost/',views.registrarPost,name="registarPost"),
    path('novedades',views.Novedades,name="novedades"),
    path('panoramas',views.Panoramas,name="panoramas"),
    path('eliminacionUsuario/<codigo>',views.eliminacionUsuario),
    path('edicionUsuario/<codigo>',views.edicionUsuario,name="edicionUsuario"),
    path('editarUsuario/',views.editarUsuario),
    path('eliminacionPost/<id>',views.eliminacionPost,name="eliminacionPost"),
    path('Posts/',views.Post,name="posts"),
    path('registrarPost/',views.registrarPost , name="registrarPost"),
    path('',views.home),
    path('carrito/',views.carrito, name="carrito"),
    path('registrarPlan/',views.registrarPlan,name='registrarPlan'),
    path('eliminacionPlan/<codigo>',views.eliminacionPlan,name="eliminacionPlan"),

]