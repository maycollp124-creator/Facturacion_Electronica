# ============================================================
# archivos.py
# Módulo de persistencia: lee y guarda los datos del sistema
# (cajeros, clientes y productos) en archivos CSV.
# ============================================================

import csv  # Librería estándar para leer/escribir archivos CSV
import os   # Para trabajar con rutas y carpetas del sistema

# Si la carpeta donde se guardan los datos no existe, se crea
if not os.path.exists("Facturacion_Electronica"):
    os.makedirs("Facturacion_Electronica")

# Rutas de los archivos CSV donde se almacena la información
RUTA_CAJEROS = "Facturacion_Electronica/cajeros.csv"
RUTA_CLIENTES = "Facturacion_Electronica/clientes.csv"
RUTA_PRODUCTOS = "Facturacion_Electronica/productos.csv"


# ---------------------- CAJEROS ----------------------

def cargar_cajeros():
    """Lee cajeros.csv y devuelve una lista de diccionarios {usuario, contraseña}."""
    cajeros = []
    # Solo se intenta leer si el archivo ya existe
    if os.path.exists(RUTA_CAJEROS):
        with open(RUTA_CAJEROS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                # Cada fila válida debe tener exactamente 2 columnas
                if len(fila) == 2:
                    cajeros.append({"usuario": fila[0], "contraseña": fila[1]})
    return cajeros


def guardar_cajeros(cajeros):
    """Sobrescribe cajeros.csv con la lista de cajeros recibida."""
    with open(RUTA_CAJEROS, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for c in cajeros:
            escritor.writerow([c["usuario"], c["contraseña"]])


# ---------------------- CLIENTES ----------------------

def cargar_clientes():
    """Lee clientes.csv y devuelve una lista de diccionarios {nombre, documento, telefono}."""
    clientes = []
    if os.path.exists(RUTA_CLIENTES):
        with open(RUTA_CLIENTES, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                # Cada fila válida debe tener 3 columnas
                if len(fila) == 3:
                    clientes.append({"nombre": fila[0], "documento": fila[1], "telefono": fila[2]})
    return clientes


def guardar_clientes(clientes):
    """Sobrescribe clientes.csv con la lista de clientes recibida."""
    with open(RUTA_CLIENTES, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for c in clientes:
            escritor.writerow([c["nombre"], c["documento"], c["telefono"]])


# ---------------------- PRODUCTOS ----------------------

def cargar_productos():
    """Lee productos.csv y devuelve una lista de diccionarios
    {codigo, nombre, precio, cantidad}."""
    productos = []
    if os.path.exists(RUTA_PRODUCTOS):
        with open(RUTA_PRODUCTOS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                # Cada fila válida debe tener 4 columnas
                if len(fila) == 4:
                    productos.append({
                        "codigo": fila[0],
                        "nombre": fila[1],
                        "precio": float(fila[2]),   # El CSV guarda texto: se convierte a decimal
                        "cantidad": int(fila[3])    # y a entero
                    })
    return productos


def guardar_productos(productos):
    """Sobrescribe productos.csv con la lista de productos recibida."""
    with open(RUTA_PRODUCTOS, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for p in productos:
            escritor.writerow([p["codigo"], p["nombre"], p["precio"], p["cantidad"]])