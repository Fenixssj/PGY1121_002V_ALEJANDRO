import time


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
['J1','J2','J3','J4'],
]

asientos_ocupados=[]
todos_asientos=[]
asiento_cliente=[]

def imprimir_asientos(ocupados):
    asiento = "Asientos disponibles \n" 
    for fila in bus:
        for columna in fila:
            todos_asientos.append(columna)
            if columna in ocupados:
                asiento += f'|--|'
            else:
                asiento += f'|{columna}|'
        asiento += '\n'
    print(asiento)
    input('')

def comprar():
    validador = True
    while validador:
        asiento = input('Elija un asiento disponible: ')
        if asiento in todos_asientos:
            if not asiento in asientos_ocupados:
                    asientos_ocupados.append(asiento)
                    cliente(asiento)
                    validador = False
            else: 
                print('Asiento no disponible, presione ENTER para continuar >')
                input('')
                validador = True
        else:
            print('asiento no existe, presione ENTER para continuar >')
            input('')
            validador = True

    
def cliente(asiento):
    print("Ingrese los siguientes datos:")
    validadorRut = True
    while validadorRut:
        rut = input("RUT(Sin puntos ni guion): ")
        if len(rut) > 10 or len(rut) < 8:
            print("RUT no valido, favor ingresar denuevo")
            time.sleep(0.5)
            validadorRut = True
        else:
            validadorRut = False

    validadorNombre = True
    while validadorNombre:
        nombre = str(input("Nombre: "))
        if len(nombre) < 3:
            print("Nombre no valido, favor ingresar denuevo")
            time.sleep(0.5)
            validadorNombre = True
        else:
            validadorNombre = False

    validadorApellido = True
    while validadorApellido:
        apellido = str(input("Apellido: "))
        if len(apellido) < 3:
            print("Apellido no valido, favor ingresar denuevo")
            time.sleep(0.5)
            validadorApellido = True
        else:
            validadorApellido = False

    validadorFono = True
    while validadorFono:
        fono = input("Telefono de emergencia: (+56)")
        if len(fono) > 10 and len(fono) < 8:
            print("Telefono no valido, favor ingresar denuevo")
            time.sleep(0.5)
            validadorFono = True
        else:
            validadorFono = False
    asiento_cliente.append([asiento,rut,nombre,apellido,fono])

def mostrarCliente(mostrarAsiento):
        
    if mostrarAsiento in todos_asientos:
        for columna in asiento_cliente:
            if columna[0] == mostrarAsiento:
                print(f"RUT: {columna[1]}")
                print(f"Nombre: {columna[2]}")
                print(f"Apellido: {columna[3]}")
                print(f"Telefono de emergencia: (+56){columna[4]}")
                print(f"Asiento: {columna[0]}")
                input("")
                
            else:
                print("El asiento no se encuentra registrado. Presione ENTER para continuar >")
    else:
        print("Asiento no existe. Presione ENTER para continuar >")
            
def mostrarTodo():
    for columna in asiento_cliente:
        print(f"-----ASIENTO {columna[0]}-----")
        print(f"Nombre: {columna[2]}")
        print(f"Apellido: {columna[3]}")
        print("-------------------------------")
    input("")

def mostrar_ganancias_totales():
    precios = {
        'Primeras 3 filas': 25000,
        'Filas 4 a la 6': 20000,
        'Filas 6 a la 10': 15000
    }
    cantidad_asientos = {
        'Primeras 3 filas': 0,
        'Filas 4 a la 6': 0,
        'Filas 6 a la 10': 0
    }

    total_ganancias = 0

    for columna in asientos_ocupados:
        for fila in columna:
            if len(fila) in range(3):
                cantidad_asientos['Primeras 3 filas'] += 1
                total_ganancias += precios['Primeras 3 filas']
            elif len(fila) in range(6):
                cantidad_asientos['Filas 4 a la 6'] += 1
                total_ganancias += precios['Filas 4 a la 6']
            else:
                cantidad_asientos['Filas 6 a la 10'] += 1
                total_ganancias += precios['Filas 6 a la 10']

    print("Ganancias totales (boleta)")
    print("--------------------------")
    print("Tipo\t\tCantidad\tTotal")
    for tipo, cantidad in cantidad_asientos.items():
        total_tipo = cantidad*precios[tipo]
        print(f"{tipo}\t\t{cantidad}\t\t{total_tipo}")

def menuGeneral():
    validador = True
    while validador:
        print("---Bienvenidos a buses---")
        print("1- Registrar nuevo viaje")
        print("2- Mostrar asiento")
        print("3- Mostrar informacion del viaje")
        print("4- Mostrar informacion de todos los viajes")
        print("5- Boleta")
        print("6- Salir")
        op=int(input("Elija una opcion: "))
        return op
    
menu = True
while menu:
    op=menuGeneral()
    if op == 1:
        print(imprimir_asientos(asientos_ocupados))
        print(comprar())
        
    if op == 2:
        print(imprimir_asientos(asientos_ocupados))

    if op == 3:
        mostrarAsiento = input("Ingrese el asiento que esta buscando: ")
        print(mostrarCliente(mostrarAsiento))
    
    if op == 4:
        print(mostrarTodo())

    if op == 5:
        print(mostrar_ganancias_totales())

    if op == 6:
        print("Hasta luego")
        print("Nicolas Reyes")
        print("14-07-2023")
        time.sleep(1)
        menu = False

