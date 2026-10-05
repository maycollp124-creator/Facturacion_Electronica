import csv
import os

if not os.path.exists("Facturacion_Electronica"):
    os.makedirs("Facturacion_Electronica")

RUTA_CAJEROS = "Facturacion_Electronica/cajeros.csv"
RUTA_CLIENTES = "Facturacion_Electronica/clientes.csv"
RUTA_PRODUCTOS = "Facturacion_Electronica/productos.csv"

def cargar_cajeros():
    cajeros = []
    if os.path.exists(RUTA_CAJEROS):
        with open(RUTA_CAJEROS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 2:
                    cajeros.append({"usuario": fila[0], "contraseña": fila[1]})
    return cajeros

def guardar_cajeros(cajeros):
    with open(RUTA_CAJEROS, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for c in cajeros:
            escritor.writerow([c["usuario"], c["contraseña"]])

def cargar_clientes():
    clientes = []
    if os.path.exists(RUTA_CLIENTES):
        with open(RUTA_CLIENTES, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 3:
                    clientes.append({"nombre": fila[0], "documento": fila[1], "telefono": fila[2]})
    return clientes

def guardar_clientes(clientes):
    with open(RUTA_CLIENTES, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for c in clientes:
            escritor.writerow([c["nombre"], c["documento"], c["telefono"]])

def cargar_productos():
    productos = []
    if os.path.exists(RUTA_PRODUCTOS):
        with open(RUTA_PRODUCTOS, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 4:
                    productos.append({
                        "codigo": fila[0],
                        "nombre": fila[1],
                        "precio": float(fila[2]),
                        "cantidad": int(fila[3])
                    })
    return productos

def guardar_productos(productos):
    with open(RUTA_PRODUCTOS, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for p in productos:
            escritor.writerow([p["codigo"], p["nombre"], p["precio"], p["cantidad"]])