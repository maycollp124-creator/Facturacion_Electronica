import os
from datetime import datetime
from validaciones import leer_entero, leer_flotante, leer_texto_no_vacio
from archivos import guardar_cajeros, guardar_clientes, guardar_productos

# Gestion de cajeros

def registrar_cajero(cajeros):
    print("\n-----------------------------------")
    print("         REGISTRAR CAJERO")
    print("-----------------------------------")
    usuario = leer_texto_no_vacio("Ingrese el usuario: ")

    for c in cajeros:
        if c["usuario"] == usuario:
            print("\nError: Ese usuario ya esta registrado.")
            return

    contraseña = leer_texto_no_vacio("Ingrese la contraseña: ")
    cajeros.append({"usuario": usuario, "contraseña": contraseña})
    guardar_cajeros(cajeros)
    print("\nCajero registrado correctamente.")

def ver_cajeros(cajeros):
    print("\n-----------------------------------")
    print("           VER CAJEROS")
    print("-----------------------------------")
    if not cajeros:
        print("\nNo hay cajeros registrados.")
        return

    for i, c in enumerate(cajeros, 1):
        print(f"\nCajero {i}")
        print(f"Usuario   : {c['usuario']}")
        print(f"Contraseña: {c['contraseña']}")

def modificar_cajero(cajeros):
    print("\n-----------------------------------")
    print("         MODIFICAR CAJERO")
    print("-----------------------------------")
    usuario_buscar = leer_texto_no_vacio("Ingrese el usuario a modificar: ")

    for c in cajeros:
        if c["usuario"] == usuario_buscar:
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

# Gestion de clientes

def registrar_cliente(clientes):
    print("\n-----------------------------------")
    print("         REGISTRAR CLIENTE")
    print("-----------------------------------")
    documento = leer_texto_no_vacio("Ingrese el documento del cliente: ")

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
    print("\n-----------------------------------")
    print("        MODIFICAR CLIENTE")
    print("-----------------------------------")
    doc = leer_texto_no_vacio("Ingrese el documento del cliente a modificar: ")

    for c in clientes:
        if c["documento"] == doc:
            c["nombre"] = leer_texto_no_vacio("Ingrese el nuevo nombre: ")
            c["telefono"] = leer_texto_no_vacio("Ingrese el nuevo telefono: ")
            guardar_clientes(clientes)
            print("\nCliente actualizado correctamente.")
            return
    print("\nNo se encontro un cliente con ese documento.")

def eliminar_cliente(clientes):
    print("\n-----------------------------------")
    print("         ELIMINAR CLIENTE")
    print("-----------------------------------")
    doc = leer_texto_no_vacio("Ingrese el documento del cliente a eliminar: ")

    for i, c in enumerate(clientes):
        if c["documento"] == doc:
            clientes.pop(i)
            guardar_clientes(clientes)
            print("\nCliente eliminado correctamente.")
            return
    print("\nNo se encontro un cliente con ese documento.")

# Gestion de productos

def registrar_producto(productos):
    print("\n-----------------------------------")
    print("         REGISTRAR PRODUCTO")
    print("-----------------------------------")
    codigo = leer_texto_no_vacio("Ingrese el codigo del producto (ej. P001): ")

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

# Reportes e inventario

def generar_reporte_estadisticas(productos):
    print("\n-----------------------------------")
    print("     REPORTES Y ESTADISTICAS")
    print("-----------------------------------")

    if not productos:
        print("\nNo hay productos para generar reportes.")
        return

    matriz_inventario = []
    total_inventario_valor = 0
    producto_mas_costoso = productos[0]
    productos_agotados = []

    for p in productos:
        valor_total_item = p["precio"] * p["cantidad"]
        total_inventario_valor += valor_total_item

        matriz_inventario.append([p["codigo"], p["nombre"], p["precio"], p["cantidad"], valor_total_item])

        if p["precio"] > producto_mas_costoso["precio"]:
            producto_mas_costoso = p

        if p["cantidad"] == 0:
            productos_agotados.append(p["nombre"])

    print(f"\n1. Valor total del inventario: ${total_inventario_valor}")
    print(f"2. Producto mas costoso     : {producto_mas_costoso['nombre']} (${producto_mas_costoso['precio']})")
    print(f"3. Cantidad de productos    : {len(productos)}")
    print(f"4. Productos agotados       : {', '.join(productos_agotados) if productos_agotados else 'Ninguno'}")

    print("\n--- MATRIZ RESUMEN DE INVENTARIO ---")
    print(f"{'CODIGO':<8} | {'NOMBRE':<20} | {'PRECIO':<10} | {'STOCK':<6} | {'SUBTOTAL':<12}")
    print("-" * 65)
    for fila in matriz_inventario:
        print(f"{fila[0]:<8} | {fila[1]:<20} | ${fila[2]:<9.2f} | {fila[3]:<6} | ${fila[4]:<11.2f}")

# Facturacion

def crear_factura(usuario, clientes, productos):
    print("\n-----------------------------------")
    print("          CREAR FACTURA")
    print("-----------------------------------")

    doc = leer_texto_no_vacio("Ingrese el documento del cliente: ")
    cliente_sel = None

    for c in clientes:
        if c["documento"] == doc:
            cliente_sel = c
            break

    if not cliente_sel:
        print("\nCliente no encontrado. Debe registrarlo primero.")
        return

    print(f"\nCliente: {cliente_sel['nombre']} | Doc: {cliente_sel['documento']}")

    productos_factura = []
    subtotal = 0

    while True:
        codigo = leer_texto_no_vacio("\nIngrese el codigo del producto (0 para terminar): ")
        if codigo == "0":
            break

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

        if cant <= 0 or cant > prod_sel["cantidad"]:
            print("Cantidad no valida o stock insuficiente.")
            continue

        valor_p = prod_sel["precio"] * cant
        productos_factura.append({
            "codigo": prod_sel["codigo"],
            "nombre": prod_sel["nombre"],
            "cantidad": cant,
            "precio": prod_sel["precio"],
            "valor": valor_p
        })

        subtotal += valor_p
        print("Producto agregado.")

    if not productos_factura:
        print("\nFactura cancelada: sin productos.")
        return

    iva = subtotal * 0.19
    total = subtotal + iva

    print("\n1. Efectivo")
    print("2. Tarjeta")
    opcion_pago = leer_texto_no_vacio("Seleccione forma de pago: ")

    efectivo = 0
    cambio = 0
    forma_pago = "Tarjeta"

    if opcion_pago == "1":
        forma_pago = "Efectivo"
        while True:
            print(f"Total a pagar: ${total}")
            efectivo = leer_flotante("Ingrese el dinero recibido: ")
            if efectivo >= total:
                cambio = efectivo - total
                break
            print(f"Falta dinero. Total a pagar es ${total}")

    num_factura = 1
    archivo_facturas = "Facturacion_Electronica/facturas.csv"

    if os.path.exists(archivo_facturas):
        with open(archivo_facturas, "r", encoding="utf-8") as f:
            for linea in f:
                if "Factura de venta: FV-" in linea:
                    num_factura += 1

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
    for det in productos_factura:
        txt_factura += f"{det['cantidad']:<6} {det['nombre']:<35} ${det['valor']}\n"

    txt_factura += f"""------------------------------------------------------------
                       SUBTOTAL:   ${subtotal}
                       IVA 19%:    ${iva}
                       TOTAL:      ${total}
------------------------------------------------------------
                    FORMA DE PAGO: {forma_pago}
"""
    if forma_pago == "Efectivo":
        txt_factura += f"Efectivo recibido:                  ${efectivo}\n"
        txt_factura += f"Cambio:                              ${cambio}\n"

    txt_factura += f"""------------------------------------------------------------
Elaborado por: {usuario}
              ¡Gracias por su compra!
============================================================
"""
    print(txt_factura)

    for det in productos_factura:
        for p in productos:
            if p["codigo"] == det["codigo"]:
                p["cantidad"] -= det["cantidad"]

    guardar_productos(productos)

    with open(archivo_facturas, "a", encoding="utf-8") as f:
        f.write(txt_factura)

    print("Factura guardada correctamente.")

# Buscar o ver facturas

def ver_facturas():
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

    with open(archivo_facturas, "r", encoding="utf-8") as f:
        contenido = f.read()

    if not contenido.strip():
        print("\nNo hay facturas registradas.")
        return

    if opcion == "1":
        print(contenido)
    elif opcion == "2":
        num = input("\nIngrese el numero de factura (ej. 1 o FV-000001): ").strip()
        
        # Formatear la busqueda al formato FV-00000X
        if not num.startswith("FV-"):
            if num.isdigit():
                num = f"FV-{num.zfill(6)}"

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