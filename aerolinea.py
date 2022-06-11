import numpy as np
lista_asientos = [str(x) for x in range(1,43)]
ar_asi = np.array(lista_asientos).reshape(7,6)
num_asiento = 0
datos_pasajero = []

def Reserva():
    for indice in range(7):
        for asiento in range(6):
            if num_asiento == ar_asi[indice,asiento]:
                ar_asi[indice,asiento] = "X"
                return ar_asi
def Asientos():

    print(" "*15,"Listado de Asientos disponibles")
    print()
    print("|	 "+ str(ar_asi[0][0]) +"	 "+ str(ar_asi[0][1]) +"	 "+ str(ar_asi[0][2])+"		 "+ str(ar_asi[0][3]) +"	 "+ str(ar_asi[0][4]) +"	 "+ str(ar_asi[0][5]) +"	|")
    print("|								|")
    print("|	 "+ str(ar_asi[1][0]) +"	 "+ str(ar_asi[1][1]) +"	 "+ str(ar_asi[1][2])+"              "+ str(ar_asi[1][3]) +"	"+ str(ar_asi[1][4]) +"	"+ str(ar_asi[1][5]) +"	|")
    print("|								|")
    print("|	"+ str(ar_asi[2][0]) +"	"+ str(ar_asi[2][1]) +"	"+ str(ar_asi[2][2])+"              "+ str(ar_asi[2][3]) +"	"+ str(ar_asi[2][4]) +"	"+ str(ar_asi[2][5]) +"	|")
    print("|								|")
    print("|	"+ str(ar_asi[3][0]) +"	"+ str(ar_asi[3][1]) +"	"+ str(ar_asi[3][2])+"              "+ str(ar_asi[3][3]) +"	"+ str(ar_asi[3][4]) +"	"+ str(ar_asi[3][5]) +"	|")
    print("|								|")
    print("|	"+ str(ar_asi[4][0]) +"	"+ str(ar_asi[4][1]) +"	"+ str(ar_asi[4][2])+"              "+ str(ar_asi[4][3]) +"	"+ str(ar_asi[4][4]) +"	"+ str(ar_asi[4][5]) +"	|")
    print("|_______________________________________________________________|")
    print("|_______________________________________________________________|")
    print("|	"+ str(ar_asi[5][0]) +"	"+ str(ar_asi[5][1]) +"	"+ str(ar_asi[5][2])+"              "+ str(ar_asi[5][3]) +"	"+ str(ar_asi[5][4]) +"	"+ str(ar_asi[5][5]) +"	|")
    print("|								|")
    print("|								|")
    print("|	"+ str(ar_asi[6][0]) +"	"+ str(ar_asi[6][1]) +"	"+ str(ar_asi[6][2])+"              "+ str(ar_asi[6][3]) +"	"+ str(ar_asi[6][4]) +"	"+ str(ar_asi[6][5]) +"	|")
    print()

def Comprar():    
    print("Abriendo menu de Ventas")
    global datos_pasajero
    global num_asiento
    global rut
    global ar_asi
    Seguir = True
    while Seguir == True:
        print("Ingrese nombre del pasajero : ")
        nombre = input()
        datos_pasajero.append(nombre)
        while True:
            try:
                rut=int(input("Ingrese su RUT (sin puntos ni guión):\n"))
                if rut >= 5000000 and rut <= 99999999:
                 datos_pasajero.append(str(rut))
                 break
                else:
                    print("Ingreso incorrecto")
            except ValueError:
                print("Ingreso incorrecto")
        while True:
            print("Ingrese número de telefono del pasajero. Ejemplo 945081197.\n")
            try:
                telefono = int(input())
                if telefono >= 1_000_000 and telefono <= 999_999_999:
                    datos_pasajero.append(str(telefono))
                    break
            except:
                print("N° ingresado no valido")
        while True:
            print("¿Es usted miembro de 'BancoDuoc'?. Digite 1 para SI, 2 para NO.\n1.- SI.\n2.- NO.")
            try:
                banco = int(input())
                if banco >= 1 and banco <=2:
                    if banco == 1:
                        datos_pasajero.append("BancoDUOC")
                        break
                    if banco == 2:
                        datos_pasajero.append("Otro Banco")
                        break
                else:
                    print("Opción no Válida, vuelva a intentarlo\n")
            except:
                print("Opcion no valida")         
        while True:
            print("Elija el número de asiento a comprar")   
            try:
                num_asiento = int(input())
                if num_asiento >= 1 and num_asiento<= 42:
                    if num_asiento >=1 and num_asiento <= 30:
                        print(f"El número de asiento {num_asiento} pertenece a la CLASE NORMAL, con un valor de $78,900.\n¿Desea continuar?\n1.- SI.\n2.- NO.")
                        op_compra = int(input())
                        if op_compra >=1 and op_compra<=2:
                            if op_compra == 1:
                                precio_asiento = 78900
                                if banco == 1:
                                    precio_asiento = precio_asiento * 0.85
                                    print(f"Por ser Banco de DuocUc, obtiene un 15% de descuento.\nTotal a pagar ${round(precio_asiento)}.\n")
                                    Seguir = False
                                    num_asiento = str(num_asiento)
                                    datos_pasajero.append(num_asiento)
                                    print("Datos reserva:")
                                    print([f'{x}' for x in datos_pasajero])
                                    Reserva()
                                    return ar_asi
                                elif banco == 2:
                                    print(f"Total a pagar ${round(precio_asiento)}.\n")
                                    Seguir = False
                                    num_asiento = str(num_asiento)
                                    datos_pasajero.append(num_asiento)
                                    print("Datos reserva:")
                                    print([f'{x}' for x in datos_pasajero])
                                    Reserva()
                                    return ar_asi
                                else:
                                  print()
                            if op_compra == 2:
                                print()
                    elif num_asiento >= 31 and num_asiento <= 42:
                        print(f"El número de asiento {num_asiento} pertenece a la CLASE VIP, con un valor de $240,000.\n¿Desea continuar?\n1.- SI.\n2.- NO.")
                        op_compra = int(input())
                        if op_compra >=1 and op_compra <=2:
                            if op_compra == 1:
                                precio_asiento = 240000
                                if banco == 1:
                                    precio_asiento = precio_asiento * 0.85
                                    print(f"Por ser Banco de DuocUc, obtiene un 15% de descuento.\nTotal a pagar ${round(precio_asiento)}.\n")
                                    Seguir = False
                                    num_asiento = str(num_asiento)
                                    datos_pasajero.append(num_asiento)
                                    print("Datos reserva:")
                                    print([f'{x}' for x in datos_pasajero])
                                    Reserva()
                                    return ar_asi
                                elif banco == 2:
                                    print(f"Total a pagar ${round(precio_asiento)}.\n")
                                    Seguir = False
                                    num_asiento = str(num_asiento)
                                    datos_pasajero.append(num_asiento)
                                    print("Datos reserva:")
                                    print([f'{x}' for x in datos_pasajero])
                                    Reserva()
                                    return ar_asi
                                else:
                                  print()
                            if op_compra == 2:
                                print()            
                else:
                    print("Número de asiento no es válido")
            except:
                print("Error en el tipo de asiento")

def Anular():
    print("Ingresando al menu de anulacion")
    global ar_asi
    global num_asiento
    global datos_pasajero
    global rut
    rut_anular = str(input("Ingrese rut del dueño de la reserva"))
    asiento_anular = int(input("ingrese el numero de asiento"))
    if asiento_anular >=1 and asiento_anular <= 42:
        asiento_anular = str(asiento_anular)
        if asiento_anular == num_asiento:
            for indice in range(7):
                for asiento in range(6):
                    if num_asiento == ar_asi[indice,asiento]:
                        ar_asi[indice,asiento] = num_asiento
            datos_pasajero = []
            num_asiento = 0
            print("Anulacion de reserva exitosa.\n")
            return ar_asi,datos_pasajero
        else:
            print("No es posible anular, asiento no está reservado.\nIntente nuevamente.\n")
    else:
        print("número de asiento no válido. Intente nuevamente.\n")
def Modificar(): 
    global datos_pasajero
    try:
        mod_rut = str(input("Ingrese el rut asignado al asiento"))
        mod_asiento = str(input("Ingrese el numero que de asiento que desee modificar"))
        if mod_asiento == datos_pasajero[4] and mod_rut == datos_pasajero[1]:
            while True:
                print("Ingrese nombre para modificar la reserva.\n")
                nombre = input()
                datos_pasajero[0] = nombre
                print("Ingrese numero de celular para modificar la reserva.\n")
                try:
                    celular = int(input())
                    datos_pasajero[2] = celular
                    print("Datos reserva:")
                    print([f'{x}' for x in datos_pasajero])
                    return datos_pasajero
                except:
                    print("Número ingresado no es válido")                
        else:
            print("Datos ingresados no concuerdan con reservaciones.  Vuelva a intentarlo.\n")
    except:
        print("Opción no válida, vuelva a intentarlo.")

def menu():
    while True:
        print("1.- Ver asientos disponibles\n2.- Comprar asiento.\n3.- Anular vuelo.\n4.- Modificar datos de pasajero.\n5.- Salir.\n")
        try:
            menu_op = int(input())
            if menu_op >= 1 and menu_op <=5:
                if menu_op == 1:
                    Asientos()
                if menu_op == 2:
                    Comprar()
                if menu_op == 3:
                    Anular()
                if menu_op == 4:
                    Modificar()
                if menu_op == 5:
                    break
            else:
                print("La opciones debe ser entre 1 a 5")
        except:
            print("Opción no válida, vuelva a intentarlo.\n")
menu()