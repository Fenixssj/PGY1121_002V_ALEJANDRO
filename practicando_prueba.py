import os

bus = [
    ['A1','A2','A3','A4'],
    ['B1','B2','B3','B4'],
    ['C1','C2','C3','C4'],
    ['D1','D2','D3','D4'],
    ['E1','E2','E3','E4'],
    ['F1','F2','F3','F4'],
    ['G1','G2','G3','G4'],
    ['H1','H2','H3','H4'],
    ['I1','I2','I3','I4'],
    ['J1','J2','J3','J4']
]

asiento_ocupado = []
asiento_disponible = []
pasaje_comprado = []

def mostrar_bus():
    dibujar_bus = "\n---------- bus ---------\n"
    for fila in bus:
        for asiento in fila:
            asiento_disponible.append(asiento)
            if asiento in asiento_ocupado:
                dibujar_bus += f"|x{asiento}x|"
            else:
                dibujar_bus += f"| {asiento} |"
        dibujar_bus += "\n"        
    dibujar_bus += "------------------------\n"
    print(dibujar_bus)


def menu_fila():
    os.system
    print("------ valores filas asientos -------")
    print("1. Primeras 3 filas: --\t $25.000 ")
    print("2. fila 4 a la 6: --\t $20.000 ")
    print("3. fila 6 a la 10: --\t $15.000 ")
    print("-------------------------------------")
    try:
        opcion = int(input("Ingrese una fila para comprar > "))
        if opcion >= 1 and opcion <= 3:
            return opcion
        else:
            input("Opcion fuera de rango, Presione enter para continuar > ")
    except:
        input("Opcion no es valida, Presione enter para continuar > ")


def registrar_viaje():
    asiento = input("ingrese el asiento que desea utilizar: ")

    if asiento in asiento_disponible:
        if not asiento in asiento_ocupado:
            asiento_ocupado.append(asiento) 
            print("Por favor ingresar los siguentes datos: ")
            origen = input("Origen : ")
            destino = input("Destino : ")
            rut = input("Rut : ")
            nombre = input("Nombre : ")
            apellido = input("Apellido : ")
            telefono_emergencia = input("Telefono de emergencia : ")

            pasaje_comprado.append(
                [asiento, origen, destino , rut, nombre, apellido, telefono_emergencia]            
            )

            input(f"Pasaje con asiento numero {asiento} fue registrado exitosamente > ")
        else:
            input("El asiento se encuentra ocupado")
    else:
        input("El asiento no existe")


def mostra_viaje():
    asiento = input("ingrese el asiento que desea visualizar: ")

    if asiento in asiento_disponible:
        if asiento in asiento_ocupado:
            
            for pasaje in pasaje_comprado:
                if pasaje[0] == asiento:
                    print(f"--------- PASAJE {pasaje[0]} ---------")
                    print(f"Origen:        {pasaje[1]}")
                    print(f"Destino:       {pasaje[2]}")
                    print(f"Rut:           {pasaje[3]}")
                    print(f"Nombre:        {pasaje[4]}")
                    print(f"Apellido:      {pasaje[5]}")
                    print(f"Telefono de emergencia: {pasaje[6]}")
                    input(f"------------------------------")

        else:
            input("El asiento se encuentra disponible para utilizar >")    
    else:
        input("El asiento no existe ")


def mostrar_todo_los_viajes():
    os.system("cls")
    for pasaje in pasaje_comprado:
        print(f"--------- PASAJE {pasaje[0]} ---------")
        print(f"Nombre:        {pasaje[2]}")
        print(f"Apellido:      {pasaje[3]}")
        print(f"------------------------------")
    input("")


def menu_general():
    os.system("cls")
    print("---------- menu general del programa -----------")
    print("1. Registrar un nuevo viaje")
    print("2. Mostrar asiento")
    print("3. Nostrar informacion dell viaje ")
    print("4. Mostrar informacion de todo los viajes ")
    print("5. Mostrar ganacias totales de los viajes (Boleta)")
    print("6. Salir del sistema ")
    print("------------------------------------------------")
    try:
        opcion = int(input("Ingrese una de las opciones disponible del menu > "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            input("Opcion fuera de rango, Presione enter para continuar > ")
    except:
        input("Opcion no es valida, Presione enter para continuar > ")


menu = True
while menu:
    opcion = menu_general()
    if opcion == 1:
        menu_fila()
        mostrar_bus()
        registrar_viaje()
    if opcion == 2:
         mostrar_bus()
         input("")
    if opcion == 3:
        mostrar_bus()
        mostra_viaje()
    if opcion == 4:
        mostrar_todo_los_viajes()
    if opcion == 5:
        input("opcion 5")
    if opcion == 6:
        os.system("cls")
        print("Salio del sistema, adios :D")
        menu = False
