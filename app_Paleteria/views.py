from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto, Venta, Proveedor, InventarioIngrediente, Empleado
from django.utils import timezone

# =====================================
# INICIO
# =====================================
def inicio_paleteria(request):
    return render(request, 'inicio.html')


# =====================================
# CRUD CLIENTE
# =====================================
def agregar_cliente(request):
    if request.method == "POST":
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            direccion=request.POST['direccion'],
            ciudad=request.POST['ciudad'],
            fecha_registro=timezone.now().date()
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')


def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('id_cliente')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})


def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})


def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == "POST":
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        cliente.telefono = request.POST.get('telefono', cliente.telefono).strip()
        cliente.email = request.POST.get('email', cliente.email).strip()
        cliente.direccion = request.POST.get('direccion', cliente.direccion).strip()
        cliente.ciudad = request.POST.get('ciudad', cliente.ciudad).strip()

        fecha_registro = request.POST.get('fecha_registro', '').strip()
        if fecha_registro:
            cliente.fecha_registro = fecha_registro

        cliente.save()
        return redirect('ver_cliente')
    return redirect('ver_cliente')


def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


# =====================================
# CRUD PRODUCTO
# =====================================
def agregar_producto(request):
    ingredientes = InventarioIngrediente.objects.all()
    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST['nombre'],
            sabor=request.POST['sabor'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            tipo=request.POST['tipo'],
            fecha_elaboracion=request.POST['fecha_elaboracion'],
            id_ingrediente_id=request.POST['id_ingrediente']
        )
        return redirect('ver_producto')
    return render(request, 'producto/agregar_producto.html', {'ingredientes': ingredientes})


def ver_producto(request):
    productos = Producto.objects.select_related('id_ingrediente').all().order_by('id_producto')
    return render(request, 'producto/ver_producto.html', {'productos': productos})


def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    ingredientes = InventarioIngrediente.objects.all()
    return render(request, 'producto/actualizar_producto.html', {
        'producto': producto,
        'ingredientes': ingredientes
    })


def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.sabor = request.POST['sabor']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.tipo = request.POST['tipo']
        if request.POST.get('fecha_elaboracion'):
            producto.fecha_elaboracion = request.POST['fecha_elaboracion']

        producto.id_ingrediente_id = request.POST['id_ingrediente']
        producto.save()
        return redirect('ver_producto')
    return redirect('ver_producto')


def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# =====================================
# CRUD EMPLEADO
# =====================================
def agregar_empleado(request):
    if request.method == "POST":
        Empleado.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            cargo=request.POST['cargo'],
            fecha_contratacion=request.POST['fecha_contratacion'],
            salario=request.POST['salario'],
            direccion=request.POST['direccion'],
            edad=request.POST['edad']
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')


def ver_empleado(request):
    empleados = Empleado.objects.all().order_by('id_empleado')
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})


def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})


def realizar_actualizacion_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == "POST":
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.cargo = request.POST['cargo']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.direccion = request.POST['direccion']
        empleado.edad = request.POST['edad']
        empleado.save()
        return redirect('ver_empleado')
    return redirect('ver_empleado')


def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})


# =====================================
# CRUD VENTA
# =====================================
def agregar_venta(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    empleados = Empleado.objects.all()
    if request.method == "POST":
        cantidad = int(request.POST['cantidad'])
        producto = Producto.objects.get(id_producto=request.POST['id_producto'])
        total = producto.precio * cantidad

        Venta.objects.create(
            fecha_venta=timezone.now().date(),
            cantidad=cantidad,
            total=total,
            metodo_pago=request.POST['metodo_pago'],
            estado=request.POST['estado'],
            observaciones=request.POST['observaciones'],
            id_cliente_id=request.POST['id_cliente'],
            id_producto_id=request.POST['id_producto'],
            id_empleado_id=request.POST['id_empleado']
        )
        return redirect('ver_venta')
    return render(request, 'venta/agregar_venta.html', {
        'clientes': clientes,
        'productos': productos,
        'empleados': empleados
    })


def ver_venta(request):
    ventas = Venta.objects.select_related('id_cliente', 'id_producto', 'id_empleado').all().order_by('id_venta')
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})


def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'venta/actualizar_venta.html', {
        'venta': venta,
        'clientes': clientes,
        'productos': productos,
        'empleados': empleados
    })


def realizar_actualizacion_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    if request.method == "POST":
        venta.cantidad = int(request.POST['cantidad'])
        venta.metodo_pago = request.POST['metodo_pago']
        venta.estado = request.POST['estado']
        venta.observaciones = request.POST['observaciones']
        venta.id_cliente_id = request.POST['id_cliente']
        venta.id_producto_id = request.POST['id_producto']
        venta.id_empleado_id = request.POST['id_empleado']
        venta.total = venta.id_producto.precio * venta.cantidad
        venta.save()
        return redirect('ver_venta')
    return redirect('ver_venta')


def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    if request.method == "POST":
        venta.delete()
        return redirect('ver_venta')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})


# =====================================
# CRUD PROVEEDOR
# =====================================
def agregar_proveedor(request):
    if request.method == "POST":
        Proveedor.objects.create(
            nombre_empresa=request.POST['nombre_empresa'],
            contacto=request.POST.get('contacto'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            descripcion=request.POST.get('descripcion')
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')


def ver_proveedor(request):
    proveedores = Proveedor.objects.all().order_by('id_proveedor')
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})


def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})


def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == "POST":
        proveedor.nombre_empresa = request.POST['nombre_empresa']
        proveedor.contacto = request.POST.get('contacto')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.descripcion = request.POST.get('descripcion')
        proveedor.save()
        return redirect('ver_proveedor')
    return redirect('ver_proveedor')


def borrar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    if request.method == "POST":
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})


# =====================================
# CRUD INGREDIENTES
# =====================================
def agregar_ingrediente(request):
    proveedores = Proveedor.objects.all()
    if request.method == "POST":
        InventarioIngrediente.objects.create(
            nombre_ingrediente=request.POST['nombre_ingrediente'],
            unidad_medida=request.POST.get('unidad_medida'),
            cantidad_actual=request.POST['cantidad_actual'],
            stock_minimo=request.POST['stock_minimo'],
            id_proveedor_id=request.POST['id_proveedor']
        )
        return redirect('ver_ingrediente')
    return render(request, 'ingrediente/agregar_ingrediente.html', {'proveedores': proveedores})


def ver_ingrediente(request):
    # Usar select_related con el nombre exacto del campo ForeignKey
    ingredientes = InventarioIngrediente.objects.select_related('id_proveedor').all().order_by('id_ingrediente')
    return render(request, 'ingrediente/ver_ingrediente.html', {'ingredientes': ingredientes})

def actualizar_ingrediente(request, id):
    ingrediente = get_object_or_404(InventarioIngrediente, id_ingrediente=id)
    proveedores = Proveedor.objects.all()
    return render(request, 'ingrediente/actualizar_ingrediente.html', {
        'ingrediente': ingrediente,
        'proveedores': proveedores
    })


def realizar_actualizacion_ingrediente(request, id):
    ingrediente = get_object_or_404(InventarioIngrediente, id_ingrediente=id)
    if request.method == "POST":
        ingrediente.nombre_ingrediente = request.POST['nombre_ingrediente']
        ingrediente.unidad_medida = request.POST.get('unidad_medida')
        ingrediente.cantidad_actual = request.POST['cantidad_actual']
        ingrediente.stock_minimo = request.POST['stock_minimo']
        ingrediente.id_proveedor_id = request.POST['id_proveedor']
        ingrediente.save()
        return redirect('ver_ingrediente')
    return redirect('ver_ingrediente')


def borrar_ingrediente(request, id):
    ingrediente = get_object_or_404(InventarioIngrediente, id_ingrediente=id)
    if request.method == "POST":
        ingrediente.delete()
        return redirect('ver_ingrediente')
    return render(request, 'ingrediente/borrar_ingrediente.html', {'ingrediente': ingrediente})
