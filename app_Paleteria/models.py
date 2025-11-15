from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    ciudad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre_empresa


# ==========================================
# MODELO: INVENTARIO DE INGREDIENTES
# ==========================================
class InventarioIngrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre_ingrediente = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=50, blank=True)
    cantidad_actual = models.IntegerField()
    stock_minimo = models.IntegerField()

    id_proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        db_column='id_proveedor'
    )

    def __str__(self):
        return f"{self.nombre_ingrediente} - {self.id_proveedor.nombre_empresa}"


# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    sabor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    tipo = models.CharField(max_length=100)
    fecha_elaboracion = models.DateField()
    descripcion = models.CharField(max_length=200, blank=True)

    id_ingrediente = models.ForeignKey(
        InventarioIngrediente,
        on_delete=models.CASCADE,
        db_column='id_ingrediente'
    )

    def __str__(self):
        return f"{self.nombre} ({self.sabor})"


# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.CharField(max_length=200)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50, blank=True)
    observaciones = models.CharField(max_length=200, blank=True)

    id_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        db_column='id_cliente'
    )

    id_producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        db_column='id_producto'
    )

    id_empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        db_column='id_empleado'
    )

    def __str__(self):
        return f"Venta {self.id_venta} - Cliente: {self.id_cliente.nombre} - Producto: {self.id_producto.nombre}"
