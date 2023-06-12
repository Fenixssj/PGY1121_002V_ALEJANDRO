import os 
# menu general:
def menu_general():
    os.system("cls")
    print("-------------------- menu general -------------------------")
    print("bienvenido al menu donitas locas, que desea llevar: ")
    print("1. donitas simples ")
    print("2. donitas con manjar y/o crema ")
    print("3. donitas con nutella ")
    print("4. boleta de las donitas ")
    print("5. salir del menu ")
    print("-----------------------------------------------------------")
    try:
        opcion = int(input("Elija su menu que deseas comprar: "))
        if opcion > 0 and opcion < 6 :
            return opcion
    except:
        print("Su opcion que eligio es invalido .")

#menu simple: 
def menu_simples():
    os.system("cls")
    print("--------------------- menu donitas simples ---------------------------")
    print("has elegido el menu donitas simples, cuantas cantidad quieres llevar: ")
    print("1. 4 donitas \t\t $1.000 ")
    print("2. 12 donitas \t\t $3.000 ")
    print("3. 24 donitas \t\t $7.000 ")
    print("4. salir del menu > ")
    print("----------------------------------------------------------------------")
    try:
        opcion = int(input("Elijs su opcion que deseas comprar :"))
        if opcion > 0 and opcion < 5 :
            return opcion
    except:
        print("Su opcion no es valido .")

# menu de manjar y crema: 
def menu_manjar_crema():
    os.system("cls")
    print("--------------- menu donitas con manajar y/o crema -------------------")
    print("has elegido el menu donitas simples, cuantas cantidad quieres llevar: ")
    print("1. 4 donitas con manjar o crema  \t\t $2.000 ")
    print("2. 12 donitas con manjar o crema \t\t $4.500 ")
    print("3. 24 donitas con manjar o crema \t\t $8.500 ")
    print("4. salir del menu > ")
    print("----------------------------------------------------------------------")
    try:
        opcion = int(input("Elijs su opcion que deseas comprar :"))
        if opcion > 0 and opcion < 5 :
            return opcion
    except:
        print("Su opcion no es valido .")


# menu con nutella:
def menu_nutella():
    os.system("cls")
    print("------------------ menu donitas con nutella --------------------------")
    print("has elegido el menu donitas simples, cuantas cantidad quieres llevar: ")
    print("1. 4 donitas con nutella  \t\t $2.500 ")
    print("2. 12 donitas con nutella \t\t $6.500 ")
    print("3. 24 donitas con nutella \t\t $10.500 ")
    print("4. salir del menu > ")
    print("----------------------------------------------------------------------")
    try:
        opcion = int(input("Elijs su opcion que deseas comprar :"))
        if opcion > 0 and opcion < 5 :
            return opcion
    except:
        print("Su opcion no es valido .")

#menu boleta:
def menu_boleta():
    subtotal = 0
    os.system("cls")
    print("------------------------ boleta del las donitas general -----------------------------")
    if simple_1 > 0:
        print(f"{simple_1} \t 4 donitas simples \t\t\t ${simple_1*1000} ")
        subtotal += simple_1*1000
    if simple_2 > 0:
        print(f"{simple_2} \t 12 donitas simples \t\t\t ${simple_2*3000} ")
        subtotal += simple_2*3000
    if simple_3 > 0:
        print(f"{simple_3} \t 24 donitas simples \t\t\t ${simple_3*7000} ")
        subtotal += simple_3*7000
    if manjar_crema_1 > 0:
        print(f"{manjar_crema_1} \t 4 donitas manjar y/o crema \t\t ${manjar_crema_1*2000} ")
        subtotal += manjar_crema_1*2000
    if manjar_crema_2 > 0:
        print(f"{manjar_crema_2} \t 12 donitas manjar y/o crema \t\t ${manjar_crema_2*4500} ")
        subtotal += manjar_crema_2*4500
    if manjar_crema_3 > 0:
        print(f"{manjar_crema_3} \t 24 donitas manjar y/o crema \t\t ${manjar_crema_3*8500} ")
        subtotal += manjar_crema_3*8500
    if nutella_1 > 0:
        print(f"{nutella_1} \t 4 donitas con nutella \t\t ${nutella_1*2500} ")
        subtotal += nutella_1*2500
    if nutella_2 > 0:
        print(f"{nutella_2} \t 12 donitas con nutella \t\t ${nutella_2*6500} ")
        subtotal += nutella_2*6500
    if nutella_3 > 0:
        print(f"{nutella_3} \t 24 donitas con nutella \t\t ${nutella_3*10500} ")
        subtotal += nutella_3*10500
    print("--------------------------------------------------------------------------------------")
    if subtotal > 0:
        print(f"subtotal \t\t\t ${subtotal}")
    else:
        print("No se ha comprado nada en el menu. > ")
    print(f"Total \t\t\t\t ${subtotal}")

def cantidad_producto():
    try:
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        if cantidad > 0 :
            return cantidad
    except:
        print("Error en ingresar la cantidad del producto aprete enter para continuar >")


#acum donitas simples:
simple_1 = 0
simple_2 = 0
simple_3 = 0

#acum donitas manjar / crema:
manjar_crema_1 = 0
manjar_crema_2 = 0
manjar_crema_3 = 0

#acum donas nutella:
nutella_1 = 0
nutella_2 = 0 
nutella_3 = 0 

menu_g = True
while menu_g:
    menu_g = menu_general()

    if menu_g == 1:
        
        menu_s = True
        while menu_s:
            menu_s = menu_simples()
            if menu_s == 1:
                simple_1 = cantidad_producto()
            if menu_s == 2:
                simple_2 = cantidad_producto()
            if menu_s == 3:
                simple_3 = cantidad_producto()
            if menu_s == 4:
                menu_s = False

    if menu_g == 2:

        menu_m_c = True
        while menu_m_c:
            menu_m_c = menu_manjar_crema()
            if menu_m_c == 1:
                manjar_crema_1 = cantidad_producto()
            if menu_m_c == 2:
                manjar_crema_2 = cantidad_producto()
            if menu_m_c == 3:
                manjar_crema_3 = cantidad_producto()
            if menu_m_c == 4:
                menu_m_c = False

    if menu_g == 3:

        menu_n = True
        while menu_n:
            menu_n = menu_nutella()
            if menu_n == 1:
                nutella_1 = cantidad_producto()
            if menu_n == 2:
                nutella_2 = cantidad_producto()
            if menu_n == 3:
                nutella_3 = cantidad_producto()
            if menu_n == 4:
                menu_n = False

    if menu_g == 4:
        menu_boleta()
        input("")

    if menu_g == 5:
        menu_g = False

print(" adios ")

        




    



