# ============================================================
# main.py
# Punto de entrada del sistema de facturación electrónica.
# Contiene el menú principal, el inicio de sesión y los menús
# del administrador y del cajero.
# ============================================================

import sys  # Necesario para usar sys.exit() y cerrar el programa

# Funciones para cargar/guardar los datos desde los archivos CSV
from archivos import (
    cargar_cajeros, guardar_cajeros,
    cargar_clientes, guardar_clientes,
    cargar_productos, guardar_productos
)
# Funciones con la lógica de negocio (registrar, ver, modificar, eliminar, facturar)
from crud import (
    registrar_cajero, ver_cajeros, modificar_cajero,
    registrar_cliente, ver_clientes, modificar_cliente, eliminar_cliente,
    registrar_producto, ver_productos, modificar_producto, eliminar_producto,
    generar_reporte_estadisticas, crear_factura, ver_facturas
)


# ---------------------- MENÚS ----------------------

def menu_administrador(cajeros, productos):
    """Menú con las opciones disponibles para el administrador."""
    while True:
        print("\n-----------------------------------")
        print("        MENU DEL ADMINISTRADOR")
        print("-----------------------------------")
        print("1. Registrar cajero")
        print("2. Ver cajeros")
        print("3. Modificar cajero")
        print("4. Gestionar Productos")
        print("5. Reportes del Inventario")
        print("6. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ").strip()

        # Se llama a la función según la opción elegida
        if opcion == "1":
            registrar_cajero(cajeros)
        elif opcion == "2":
            ver_cajeros(cajeros)
        elif opcion == "3":
            modificar_cajero(cajeros)
        elif opcion == "4":
            menu_gestion_productos(productos)
        elif opcion == "5":
            generar_reporte_estadisticas(productos)
        elif opcion == "6":
            print("\nRegresando al menu principal...")
            break  # Sale del bucle y vuelve al menú principal
        else:
            print("\nOpcion no valida.")


def menu_gestion_productos(productos):
    """Submenú del administrador para modificar o eliminar productos."""
    while True:
        print("\n-----------------------------------")
        print("       GESTION DE PRODUCTOS")
        print("-----------------------------------")
        print("1. Modificar producto")
        print("2. Eliminar producto")
        print("3. Volver")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            modificar_producto(productos)
        elif opcion == "2":
            eliminar_producto(productos)
        elif opcion == "3":
            break  # Vuelve al menú del administrador
        else:
            print("\nOpcion no valida.")


def menu_cajero(usuario, clientes, productos):
    """Menú con las opciones disponibles para el cajero que inició sesión."""
    while True:
        print("\n-----------------------------------")
        print(f"   MENU DEL CAJERO (Usuario: {usuario})")
        print("-----------------------------------")
        print("1. Registrar cliente")
        print("2. Ver clientes")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Registrar producto")
        print("6. Ver productos")
        print("7. Crear factura")
        print("8. Ver facturas")
        print("9. Cerrar sesion")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_cliente(clientes)
        elif opcion == "2":
            ver_clientes(clientes)
        elif opcion == "3":
            modificar_cliente(clientes)
        elif opcion == "4":
            eliminar_cliente(clientes)
        elif opcion == "5":
            registrar_producto(productos)
        elif opcion == "6":
            ver_productos(productos)
        elif opcion == "7":
            # Se pasa el usuario para que quede registrado en la factura ("Elaborado por")
            crear_factura(usuario, clientes, productos)
        elif opcion == "8":
            ver_facturas()
        elif opcion == "9":
            print("\nCerrando sesion...")
            break  # Cierra la sesión y vuelve al menú principal
        else:
            print("\nOpcion no valida.")


# ---------------------- INICIO DE SESIÓN ----------------------

def iniciar_sesion_administrador(cajeros, productos):
    """Valida las credenciales del administrador (fijas en el código)."""
    print("\n-----------------------------------")
    print("      INICIO DE SESION ADMIN")
    print("-----------------------------------")
    usuario = input("Usuario: ").strip()
    clave = input("Contraseña: ").strip()

    # El administrador tiene usuario y clave predefinidos
    if usuario == "admin" and clave == "3408042":
        print("\nInicio de sesion exitoso.")
        menu_administrador(cajeros, productos)
    else:
        print("\nUsuario o contraseña incorrectos.")


def iniciar_sesion_cajero(cajeros, clientes, productos):
    """Valida usuario y contraseña contra la lista de cajeros registrados."""
    print("\n-----------------------------------")
    print("     INICIO DE SESION CAJERO")
    print("-----------------------------------")
    usuario = input("Usuario: ").strip()
    clave = input("Contraseña: ").strip()

    # Se busca un cajero cuyas credenciales coincidan
    for c in cajeros:
        if c["usuario"] == usuario and c["contraseña"] == clave:
            print(f"\nBienvenido {usuario}")
            menu_cajero(usuario, clientes, productos)
            return

    # Si el bucle termina sin coincidencias, las credenciales son incorrectas
    print("\nUsuario o contraseña incorrectos.")


# ---------------------- PROGRAMA PRINCIPAL ----------------------

def main():
    """Carga los datos desde los CSV y muestra el menú principal."""
    print("============================================================")
    print("    BIENVENIDO AL SISTEMA DE FACTURACION ELECTRONICA")
    print("============================================================")

    # Los datos se cargan una sola vez y se comparten entre los menús
    cajeros = cargar_cajeros()
    clientes = cargar_clientes()
    productos = cargar_productos()

    while True:
        print("\n============================================================")
        print("      SISTEMA DE FACTURACION ELECTRONICA - INICIO")
        print("============================================================")
        print("1. Administrador")
        print("2. Cajero")
        print("3. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            iniciar_sesion_administrador(cajeros, productos)
        elif opcion == "2":
            iniciar_sesion_cajero(cajeros, clientes, productos)
        elif opcion == "3":
            print("\nGracias por usar el sistema.")
            sys.exit()  # Termina el programa
        else:
            print("\nOpcion no valida.")


# Solo ejecuta main() si el archivo se corre directamente (no si se importa)
if __name__ == "__main__":
    main()