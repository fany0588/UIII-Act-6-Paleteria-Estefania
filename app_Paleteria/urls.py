from django.urls import path
from . import views

urlpatterns = [
    # --- INICIO ---
    path('', views.inicio_paleteria, name='inicio_paleteria'),

    # ================================
    # ------- CLIENTE ---------------
    # ================================
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_cliente, name='ver_cliente'),
    path('cliente/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # ================================
    # ------- PRODUCTO --------------
    # ================================
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_producto, name='ver_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),

    # ================================
    # ------- EMPLEADO --------------
    # ================================
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/ver/', views.ver_empleado, name='ver_empleado'),
    path('empleado/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # ================================
    # ------- VENTA -----------------
    # ================================
    path('venta/agregar/', views.agregar_venta, name='agregar_venta'),
    path('venta/ver/', views.ver_venta, name='ver_venta'),
    path('venta/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('venta/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('venta/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),

    # ================================
    # ------- PROVEEDOR -------------
    # ================================
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedor/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # ==========================================
    # ------- INVENTARIO INGREDIENTES ----------
    # ==========================================
    path('ingrediente/agregar/', views.agregar_ingrediente, name='agregar_ingrediente'),
    path('ingrediente/ver/', views.ver_ingrediente, name='ver_ingrediente'),
    path('ingrediente/actualizar/<int:id>/', views.actualizar_ingrediente, name='actualizar_ingrediente'),
    path('ingrediente/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_ingrediente, name='realizar_actualizacion_ingrediente'),
    path('ingrediente/borrar/<int:id>/', views.borrar_ingrediente, name='borrar_ingrediente'),
]
