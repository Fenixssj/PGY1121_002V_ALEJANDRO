import os

bus = [
    ['A1','A2','A3','A4'],
    ['B1','B2','B3','B4'],
    ['C1','C2','C3','C4'],
    ['D1','D2','D3','D4'],
    ['F1','F2','F3','F4'],
    ['H1','H2','H3','H4'],
    ['I1','I2','I3','I4'],
    ['J1','J2','J3','J4'],
    ['K1','K2','K3','K4'],
    ['L1','L2','L3','L4'],
    ['M1','M2','M3','M4'],
    ['N1','N2','N3','N4'],
    ['Ñ1','Ñ2','Ñ3','Ñ4']
]

asientos_disponible = []
asientos_ocupado = []
pasajes_comprado = []


def mostrar_bus():    
    dibujar_bus = "\n--------- bus ----------\n"
    for fila in bus:
        for asiento in fila:
            asientos_disponible.append(asiento)
            if asiento in asientos_ocupado:
                dibujar_bus += f" +{asiento}+ "
            else:
                dibujar_bus += f"| {asiento} |"        
        dibujar_bus += "\n"
    dibujar_bus += "------------------------\n"    
    print(dibujar_bus)


def registrar_viaje():
    asiento = input("ingrese el asiento que desea utilizar: ")

    if asiento in asientos_disponible:
        if not asiento in asientos_ocupado:
            asientos_ocupado.append(asiento) 
            print("Por favor ingresar los siguentes datos: ")
            origen = input("Origen : ")
            destino = input("Destino : ")
            rut = input("Rut : ")
            nombre = input("Nombre : ")
            apellido = input("Apellido : ")
            direccion = input("Direccion : ")
            telefono_emergencia = input("Telefono de emergencia : ")

            pasajes_comprado.append(
                [asiento, origen, destino , rut, nombre, apellido, direccion, telefono_emergencia]
                #   0       1        2       3      4        5          6              7
            )

            input(f"Pasaje con asiento numero {asiento} fue registrado exitosamente > ")
        else:
            input("El asiento se encuentra ocupado")
    else:
        input("El asiento no existe")


def mostra_viaje():
    asiento = input("ingrese el asiento que desea visualizar: ")

    if asiento in asientos_disponible:
        if asiento in asientos_ocupado:
            
            for pasaje in pasajes_comprado:
                if pasaje[0] == asiento:
                    print(f"--------- PASAJE {pasaje[0]} ---------")
                    print(f"Origen:        {pasaje[1]}")
                    print(f"Destino:       {pasaje[2]}")
                    print(f"Rut:           {pasaje[3]}")
                    print(f"Nombre:        {pasaje[4]}")
                    print(f"Apellido:      {pasaje[5]}")
                    print(f"Direccion:     {pasaje[6]}")
                    print(f"Telefono de emergencia: {pasaje[7]}")
                    input(f"------------------------------")

        else:
            input("El asiento se encuentra disponible para utilizar >")    
    else:
        input("El asiento no existe ")


def mostrar_todo_los_viajes():
    os.system("cls")
    for pasaje in pasajes_comprado:
        print(f"--------- PASAJE {pasaje[0]} ---------")
        print(f"Nombre:        {pasaje[4]}")
        print(f"Apellido:      {pasaje[5]}")
        print(f"------------------------------")
    input("")


def menu_general():
    os.system("cls")
    print("---------- MENU ------------")
    print("1. Registrar viajes")
    print("2. Mostrar Asientos")
    print("3. Mostrar informacion de un viaje")
    print("4. Mostrar informacion de todo los viajes")
    print("5. Salir del sistema")
    try:
        opcion = int(input("Ingrese una de las opciones disponible > "))
        if opcion >= 1 and opcion <= 5:
            return opcion
        else:
            input("Opcion fuera de rango, Presione enter para continuar > ")
    except:
        input("Opcion no es valida, Presione enter para continuar > ")


menu = True
while menu:
    opcion = menu_general()
    if opcion == 1:
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
        os.system("cls")
        print("Salio del sistema, adios")
        menu = False