# ============================================================
# validaciones.py
# Funciones auxiliares para leer datos del usuario por consola
# validando el tipo de dato. Si la entrada es incorrecta,
# vuelven a pedirla hasta que sea válida.
# ============================================================

def leer_entero(mensaje):
    """Pide un número entero. Repite la pregunta hasta que se ingrese uno válido."""
    while True:
        try:
            valor = int(input(mensaje))  # Intenta convertir el texto a entero
            return valor
        except ValueError:
            # Se ejecuta si el texto no es un entero (ej. letras o decimales)
            print("\nError: Debe ingresar un numero entero valido.")


def leer_flotante(mensaje):
    """Pide un número decimal mayor que 0 (usado para precios y dinero recibido)."""
    while True:
        try:
            valor = float(input(mensaje))  # Intenta convertir el texto a decimal
            if valor <= 0:
                # Se rechazan valores cero o negativos
                print("\nError: El valor debe ser mayor a 0.")
            else:
                return valor
        except ValueError:
            print("\nError: Debe ingresar un numero valido.")


def leer_texto_no_vacio(mensaje):
    """Pide un texto y no permite dejarlo vacío (ignora espacios al inicio y al final)."""
    while True:
        texto = input(mensaje).strip()  # strip() elimina espacios sobrantes
        if len(texto) == 0:
            print("\nError: Este campo no puede estar vacio.")
        else:
            return texto