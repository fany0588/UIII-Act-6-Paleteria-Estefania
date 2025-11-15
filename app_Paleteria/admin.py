from django.contrib import admin
from .models import Cliente, Producto, Venta, Proveedor, InventarioIngrediente, Empleado

# ==============================
# ADMIN CLIENTE
# ==============================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'ciudad', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'telefono', 'email', 'ciudad')


# ==============================
# ADMIN PRODUCTO
# ==============================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'sabor', 'precio', 'stock', 'tipo', 'fecha_elaboracion', 'descripcion', 'id_ingrediente')
    search_fields = ('nombre', 'sabor', 'tipo')


# ==============================
# ADMIN VENTA
# ==============================
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id_venta', 'fecha_venta', 'cantidad', 'total', 'metodo_pago', 'estado', 'id_cliente', 'id_producto', 'id_empleado')
    search_fields = ('id_cliente__nombre', 'id_producto__nombre','id_empleado__nombre', 'metodo_pago', 'estado')


# ==============================
# ADMIN PROVEEDOR
# ==============================
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre_empresa', 'contacto', 'telefono', 'email', 'descripcion')
    search_fields = ('nombre_empresa', 'contacto', 'telefono', 'email')


# ===========================================
# ADMIN INVENTARIO INGREDIENTES
# ===========================================
@admin.register(InventarioIngrediente)
class InventarioIngredienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_ingrediente',
        'nombre_ingrediente',
        'unidad_medida',
        'cantidad_actual',
        'stock_minimo',
        'id_proveedor'   # Aquí estaba "proveedor", lo cambiamos
    )
    search_fields = ('nombre_ingrediente', 'id_proveedor__nombre_empresa')
    list_filter = ('id_proveedor',)  # También se cambia


# ==============================
# ADMIN EMPLEADO
# ==============================
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'apellido', 'cargo', 'fecha_contratacion', 'salario', 'edad')
    list_filter = ('cargo',)
    search_fields = ('nombre', 'apellido')
