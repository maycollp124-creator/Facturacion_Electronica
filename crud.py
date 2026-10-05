# ============================================================
# crud.py
# Lógica principal del sistema: gestión (crear, ver, modificar,
# eliminar) de cajeros, clientes y productos, además de los
# reportes de inventario y la facturación.
# ============================================================
 
import os
from datetime import datetime  # Para registrar la fecha y hora de cada factura
from validaciones import leer_entero, leer_flotante, leer_texto_no_vacio
from archivos import guardar_cajeros, guardar_clientes, guardar_productos
 
# ============================================================
# GESTIÓN DE CAJEROS
# ============================================================
 
def registrar_cajero(cajeros):
    """Registra un nuevo cajero. El usuario debe ser único."""
    print("\n-----------------------------------")
    print("         REGISTRAR CAJERO")
    print("-----------------------------------")
    usuario = leer_texto_no_vacio("Ingrese el usuario: ")
 
    # Se verifica que el usuario no exista ya
    for c in cajeros:
        if c["usuario"] == usuario:
            print("\nError: Ese usuario ya esta registrado.")
            return
 
    contraseña = leer_texto_no_vacio("Ingrese la contraseña: ")
    cajeros.append({"usuario": usuario, "contraseña": contraseña})
    guardar_cajeros(cajeros)  # Se persiste el cambio en el CSV
    print("\nCajero registrado correctamente.")
 
 
def ver_cajeros(cajeros):
    """Muestra en pantalla todos los cajeros registrados."""
    print("\n-----------------------------------")
    print("           VER CAJEROS")
    print("-----------------------------------")
    if not cajeros:
        print("\nNo hay cajeros registrados.")
        return
 
    # enumerate(..., 1) numera la lista empezando en 1
    for i, c in enumerate(cajeros, 1):
        print(f"\nCajero {i}")
        print(f"Usuario   : {c['usuario']}")
        print(f"Contraseña: {c['contraseña']}")
 
 
def modificar_cajero(cajeros):
    """Modifica usuario y contraseña de un cajero. Exige la clave del administrador."""
    print("\n-----------------------------------")
    print("         MODIFICAR CAJERO")
    print("-----------------------------------")
    usuario_buscar = leer_texto_no_vacio("Ingrese el usuario a modificar: ")
 
    for c in cajeros:
        if c["usuario"] == usuario_buscar:
            # Confirmación extra: solo el administrador puede hacer el cambio
            vali = input("Ingrese contraseña de administrador: ")
            if vali == "3408042":
                c["usuario"] = leer_texto_no_vacio("Ingrese nuevo usuario: ")
                c["contraseña"] = leer_texto_no_vacio("Ingrese nueva contraseña: ")
                guardar_cajeros(cajeros)
                print("\nCajero modificado correctamente.")
            else:
                print("\nContraseña incorrecta.")
            return
    print("\nNo se encontro un cajero con ese usuario.")
 
 
# ============================================================
# GESTIÓN DE CLIENTES
# ============================================================
 
def registrar_cliente(clientes):
    """Registra un nuevo cliente. El documento debe ser único."""
    print("\n-----------------------------------")
    print("         REGISTRAR CLIENTE")
    print("-----------------------------------")
    documento = leer_texto_no_vacio("Ingrese el documento del cliente: ")
 
    # Se evita duplicar clientes con el mismo documento
    for c in clientes:
        if c["documento"] == documento:
            print("\nError: Ese documento ya esta registrado.")
            return
 
    nombre = leer_texto_no_vacio("Ingrese el nombre del cliente: ")
    telefono = leer_texto_no_vacio("Ingrese el telefono del cliente: ")
 
    clientes.append({"nombre": nombre, "documento": documento, "telefono": telefono})
    guardar_clientes(clientes)
    print("\nCliente registrado correctamente.")
 
 
def ver_clientes(clientes):
    """Muestra en pantalla todos los clientes registrados."""
    print("\n-----------------------------------")
    print("           VER CLIENTES")
    print("-----------------------------------")
    if not clientes:
        print("\nNo hay clientes registrados.")
        return
 
    for i, c in enumerate(clientes, 1):
        print(f"\nCliente {i}")
        print(f"Nombre   : {c['nombre']}")
        print(f"Documento: {c['documento']}")
        print(f"Telefono : {c['telefono']}")
 
 
def modificar_cliente(clientes):
    """Busca un cliente por documento y actualiza su nombre y teléfono."""
    print("\n-----------------------------------")
    print("        MODIFICAR CLIENTE")
    print("-----------------------------------")
    doc = leer_texto_no_vacio("Ingrese el documento del cliente a modificar: ")
 
    for c in clientes:
        if c["documento"] == doc:
            # El documento no se modifica, solo nombre y teléfono
            c["nombre"] = leer_texto_no_vacio("Ingrese el nuevo nombre: ")
            c["telefono"] = leer_texto_no_vacio("Ingrese el nuevo telefono: ")
            guardar_clientes(clientes)
            print("\nCliente actualizado correctamente.")
            return
    print("\nNo se encontro un cliente con ese documento.")
 
 
def eliminar_cliente(clientes):
    """Elimina un cliente buscándolo por su documento."""
    print("\n-----------------------------------")
    print("         ELIMINAR CLIENTE")
    print("-----------------------------------")
    doc = leer_texto_no_vacio("Ingrese el documento del cliente a eliminar: ")
 
    for i, c in enumerate(clientes):
        if c["documento"] == doc:
            clientes.pop(i)  # Se quita de la lista por su posición
            guardar_clientes(clientes)
            print("\nCliente eliminado correctamente.")
            return
    print("\nNo se encontro un cliente con ese documento.")
 
 
# ============================================================
# GESTIÓN DE PRODUCTOS
# ============================================================
 
def registrar_producto(productos):
    """Registra un nuevo producto. El código debe ser único."""
    print("\n-----------------------------------")
    print("         REGISTRAR PRODUCTO")
    print("-----------------------------------")
    codigo = leer_texto_no_vacio("Ingrese el codigo del producto (ej. P001): ")
 
    # Se evita repetir códigos de producto
    for p in productos:
        if p["codigo"] == codigo:
            print("\nError: Ese codigo ya existe.")
            return
 
    nombre = leer_texto_no_vacio("Ingrese el nombre del producto: ")
    precio = leer_flotante("Ingrese el precio del producto: ")
    cantidad = leer_entero("Ingrese la cantidad disponible: ")
 
    productos.append({"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad})
    guardar_productos(productos)
    print("\nProducto registrado correctamente.")
 
 
def ver_productos(productos):
    """Muestra en pantalla todos los productos registrados."""
    print("\n-----------------------------------")
    print("           VER PRODUCTOS")
    print("-----------------------------------")
    if not productos:
        print("\nNo hay productos registrados.")
        return
 
    for i, p in enumerate(productos, 1):
        print(f"\nProducto {i}")
        print(f"Codigo  : {p['codigo']}")
        print(f"Nombre  : {p['nombre']}")
        print(f"Precio  : ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
 
 
def modificar_producto(productos):
    """Busca un producto por código y actualiza nombre, precio y cantidad."""
    print("\n-----------------------------------")
    print("        MODIFICAR PRODUCTO")
    print("-----------------------------------")
    codigo = leer_texto_no_vacio("Ingrese el codigo del producto a modificar: ")
 
    for p in productos:
        if p["codigo"] == codigo:
            p["nombre"] = leer_texto_no_vacio("Ingrese el nuevo nombre: ")
            p["precio"] = leer_flotante("Ingrese el nuevo precio: ")
            p["cantidad"] = leer_entero("Ingrese la nueva cantidad: ")
            guardar_productos(productos)
            print("\nProducto modificado correctamente.")
            return
    print("\nNo se encontro un producto con ese codigo.")
 
 
def eliminar_producto(productos):
    """Elimina un producto buscándolo por su código."""
    print("\n-----------------------------------")
    print("        ELIMINAR PRODUCTO")
    print("-----------------------------------")
    codigo = leer_texto_no_vacio("Ingrese el codigo del producto a eliminar: ")
 
    for i, p in enumerate(productos):
        if p["codigo"] == codigo:
            productos.pop(i)
            guardar_productos(productos)
            print("\nProducto eliminado correctamente.")
            return
    print("\nNo se encontro un producto con ese codigo.")
 
 
# ============================================================
# REPORTES E INVENTARIO
# ============================================================
 
def generar_reporte_estadisticas(productos):
    """Calcula y muestra estadísticas del inventario:
    valor total, producto más costoso, cantidad de productos y agotados."""
    print("\n-----------------------------------")
    print("     REPORTES Y ESTADISTICAS")
    print("-----------------------------------")
 
    if not productos:
        print("\nNo hay productos para generar reportes.")
        return
 
    matriz_inventario = []                # Cada fila: [codigo, nombre, precio, stock, subtotal]
    total_inventario_valor = 0            # Acumulador del valor total del inventario
    producto_mas_costoso = productos[0]   # Se parte del primero y se compara con el resto
    productos_agotados = []               # Nombres de productos con stock 0
 
    for p in productos:
        # Valor del producto en inventario = precio * unidades disponibles
        valor_total_item = p["precio"] * p["cantidad"]
        total_inventario_valor += valor_total_item
 
        matriz_inventario.append([p["codigo"], p["nombre"], p["precio"], p["cantidad"], valor_total_item])
 
        # Se actualiza el producto más costoso si este lo supera
        if p["precio"] > producto_mas_costoso["precio"]:
            producto_mas_costoso = p
 
        # Se registra como agotado si no quedan unidades
        if p["cantidad"] == 0:
            productos_agotados.append(p["nombre"])
 
    print(f"\n1. Valor total del inventario: ${total_inventario_valor}")
    print(f"2. Producto mas costoso     : {producto_mas_costoso['nombre']} (${producto_mas_costoso['precio']})")
    print(f"3. Cantidad de productos    : {len(productos)}")
    print(f"4. Productos agotados       : {', '.join(productos_agotados) if productos_agotados else 'Ninguno'}")
 
    # Tabla resumen con columnas alineadas (<N = alineado a la izquierda con ancho N)
    print("\n--- MATRIZ RESUMEN DE INVENTARIO ---")
    print(f"{'CODIGO':<8} | {'NOMBRE':<20} | {'PRECIO':<10} | {'STOCK':<6} | {'SUBTOTAL':<12}")
    print("-" * 65)
    for fila in matriz_inventario:
        print(f"{fila[0]:<8} | {fila[1]:<20} | ${fila[2]:<9.2f} | {fila[3]:<6} | ${fila[4]:<11.2f}")
 
 
# ============================================================
# FACTURACIÓN
# ============================================================
 
def crear_factura(usuario, clientes, productos):
    """Crea una factura: selecciona cliente, agrega productos, calcula IVA y total,
    procesa el pago, descuenta el stock y guarda la factura en un archivo."""
    print("\n-----------------------------------")
    print("          CREAR FACTURA")
    print("-----------------------------------")
 
    # --- 1. Buscar el cliente ---
    doc = leer_texto_no_vacio("Ingrese el documento del cliente: ")
    cliente_sel = None
 
    for c in clientes:
        if c["documento"] == doc:
            cliente_sel = c
            break
 
    # Si no existe, no se puede facturar
    if not cliente_sel:
        print("\nCliente no encontrado. Debe registrarlo primero.")
        return
 
    print(f"\nCliente: {cliente_sel['nombre']} | Doc: {cliente_sel['documento']}")
 
    # --- 2. Agregar productos a la factura ---
    productos_factura = []  # Detalle de lo que se va comprando
    subtotal = 0            # Suma de los valores antes de IVA
 
    while True:
        codigo = leer_texto_no_vacio("\nIngrese el codigo del producto (0 para terminar): ")
        if codigo == "0":
            break  # El usuario terminó de agregar productos
 
        # Buscar el producto por código
        prod_sel = None
        for p in productos:
            if p["codigo"] == codigo:
                prod_sel = p
                break
 
        if not prod_sel:
            print("Producto no encontrado.")
            continue
 
        print(f"Seleccionado: {prod_sel['nombre']} | Precio: ${prod_sel['precio']} | Stock: {prod_sel['cantidad']}")
        cant = leer_entero("Ingrese la cantidad a comprar: ")
 
        # La cantidad debe ser positiva y no superar el stock disponible
        if cant <= 0 or cant > prod_sel["cantidad"]:
            print("Cantidad no valida o stock insuficiente.")
            continue
 
        valor_p = prod_sel["precio"] * cant  # Valor de esta línea de la factura
        productos_factura.append({
            "codigo": prod_sel["codigo"],
            "nombre": prod_sel["nombre"],
            "cantidad": cant,
            "precio": prod_sel["precio"],
            "valor": valor_p
        })
 
        subtotal += valor_p
        print("Producto agregado.")
 
    # Si no se agregó ningún producto, se cancela la factura
    if not productos_factura:
        print("\nFactura cancelada: sin productos.")
        return
 
    # --- 3. Cálculo de impuestos y total ---
    iva = subtotal * 0.19   # IVA del 19 %
    total = subtotal + iva
 
    # --- 4. Forma de pago ---
    print("\n1. Efectivo")
    print("2. Tarjeta")
    opcion_pago = leer_texto_no_vacio("Seleccione forma de pago: ")
 
    efectivo = 0
    cambio = 0
    forma_pago = "Tarjeta"  # Por defecto se asume tarjeta
 
    if opcion_pago == "1":
        forma_pago = "Efectivo"
        # Se repite hasta que el dinero recibido cubra el total
        while True:
            print(f"Total a pagar: ${total}")
            efectivo = leer_flotante("Ingrese el dinero recibido: ")
            if efectivo >= total:
                cambio = efectivo - total
                break
            print(f"Falta dinero. Total a pagar es ${total}")
 
    # --- 5. Número consecutivo de factura ---
    # Se cuentan las facturas ya guardadas para asignar el siguiente número
    num_factura = 1
    archivo_facturas = "Facturacion_Electronica/facturas.csv"
 
    if os.path.exists(archivo_facturas):
        with open(archivo_facturas, "r", encoding="utf-8") as f:
            for linea in f:
                if "Factura de venta: FV-" in linea:
                    num_factura += 1
 
    # --- 6. Construcción del texto de la factura ---
    fecha = datetime.now().strftime("%Y/%m/%d %H:%M")
    txt_factura = f"""
============================================================
                 SISTEMA FAC.ELEC S.A.S.
                    NIT: 123456789-0
============================================================
Factura de venta: FV-{str(num_factura).zfill(6)}
Fecha       : {fecha}
Cliente     : {cliente_sel['nombre']}
C.C. / NIT  : {cliente_sel['documento']}
Telefono    : {cliente_sel['telefono']}
------------------------------------------------------------
CT     Descripcion                         Valor
------------------------------------------------------------
"""
    # Una línea por cada producto comprado
    for det in productos_factura:
        txt_factura += f"{det['cantidad']:<6} {det['nombre']:<35} ${det['valor']}\n"
 
    txt_factura += f"""------------------------------------------------------------
                       SUBTOTAL:   ${subtotal}
                       IVA 19%:    ${iva}
                       TOTAL:      ${total}
------------------------------------------------------------
                    FORMA DE PAGO: {forma_pago}
"""
    # Si fue en efectivo, se muestra lo recibido y el cambio
    if forma_pago == "Efectivo":
        txt_factura += f"Efectivo recibido:                  ${efectivo}\n"
        txt_factura += f"Cambio:                              ${cambio}\n"
 
    txt_factura += f"""------------------------------------------------------------
Elaborado por: {usuario}
              ¡Gracias por su compra!
============================================================
"""
    print(txt_factura)
 
    # --- 7. Descontar del inventario lo vendido ---
    for det in productos_factura:
        for p in productos:
            if p["codigo"] == det["codigo"]:
                p["cantidad"] -= det["cantidad"]
 
    guardar_productos(productos)  # Se guarda el nuevo stock
 
    # --- 8. Guardar la factura (modo "a": agrega al final sin borrar las anteriores) ---
    with open(archivo_facturas, "a", encoding="utf-8") as f:
        f.write(txt_factura)
 
    print("Factura guardada correctamente.")
 
 
# ============================================================
# CONSULTA DE FACTURAS
# ============================================================
 
def ver_facturas():
    """Permite ver todas las facturas o buscar una por su número."""
    archivo_facturas = "Facturacion_Electronica/facturas.csv"
    if not os.path.exists(archivo_facturas):
        print("\nNo hay facturas registradas.")
        return
 
    print("\n-----------------------------------")
    print("         CONSULTAR FACTURAS")
    print("-----------------------------------")
    print("1. Ver todas las facturas")
    print("2. Buscar factura por numero")
 
    opcion = input("\nSeleccione una opcion: ").strip()
 
    # Se lee todo el archivo de facturas
    with open(archivo_facturas, "r", encoding="utf-8") as f:
        contenido = f.read()
 
    if not contenido.strip():
        print("\nNo hay facturas registradas.")
        return
 
    if opcion == "1":
        print(contenido)
    elif opcion == "2":
        num = input("\nIngrese el numero de factura (ej. 1 o FV-000001): ").strip()
 
        # Si el usuario escribe solo el número (ej. 1), se convierte a FV-000001
        if not num.startswith("FV-"):
            if num.isdigit():
                num = f"FV-{num.zfill(6)}"
 
        # Las facturas están separadas por la línea de "=": se divide el contenido en bloques
        facturas = contenido.split("============================================================")
        encontrada = False
 
        for f in facturas:
            if f"Factura de venta: {num}" in f:
                print("\n============================================================")
                print(f)
                print("============================================================")
                encontrada = True
                break
 
        if not encontrada:
            print(f"\nNo se encontro la factura {num}.")
    else:
        print("\nOpcion no valida.")