def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("\nError: Debe ingresar un numero entero valido.")

def leer_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("\nError: El valor debe ser mayor a 0.")
            else:
                return valor
        except ValueError:
            print("\nError: Debe ingresar un numero valido.")

def leer_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()
        if len(texto) == 0:
            print("\nError: Este campo no puede estar vacio.")
        else:
            return texto