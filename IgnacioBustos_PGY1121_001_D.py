import os
os.system("cls")

ubicaciones=[True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True,
             True,True,True,True,True,True,True,True,True,True]
reservas=[]
ganancias_totales=0
rut_guardados=[]
valor_silver=(50000)
valor_gold=(80000)
valor_platinum=(120000)

def comprar_entrada(nombre,rut): #1
    print("ubicaciones disponibles: ")
    for i in range(len(ubicaciones)):
        if ubicaciones[i]:
            print(f"Asiento {i+1}")
    ubicacion = int(input("Ingrese el número de asiento que desea comprar: ")) -1
    if ubicaciones[ubicacion] == True:
        ubicaciones[ubicacion] = False
        reservas.append([rut,nombre,rut])
        rut_guardados.append([rut])
        print("Compra exitosa")
    else:
        print("El asiento seleccionado ya está en uso!!")

def ver_listado(): #3 MOSTRAR RUT
    print("ubicaciones disponibles: ")
    for i in range(len(ubicaciones)):
        if ubicaciones[i]:
            print(f"Asiento {i+1}, Rut:")

def ubicaciones_disponibles(): #2 solo ubicaciones disponibles
    print("ubicaciones disponibles: ")
    for i in range(len(ubicaciones)):
        if ubicaciones[i]:
            print(f"Asiento {i+1}")

def no_valido(): #5
    print("""
             Ingrese una opcion valida!!
             Volviendo al menú...""")

def ganancias(reservas): #4
    for reserva in reservas:
        if reserva[0] == rut:
            print(f"su boleta total serán: ")
        else:
            print("Usted no ha comprado ninguna entrada o se equivocó al escribir su nombre.")           


while True:
    op=input("""\n******MENÚ EVENTOS "Creativos.cl"******
    
    1-Comprar entrada
    2-Mostrar ubicaciones disponibles
    3-Ver listado de asistentes
    4-Mostrar ganancias totales

    5-Salir

Opcion: """)
    
    match op:
        case "1":
            while True:
                nombre=input("Ingrese su nombre:")
                rut=input("Ingrese su RUT: ")
                comprar_entrada(nombre,rut)
                break
        case "2":
            ubicaciones_disponibles()
            break
        case "3":
            while True:
                ver_listado()
                break
        case "4":
            while True:
                rut=input("Ingrese el nombre con el que compró las entradas: ")
                ganancias(reservas)
                break
        case "5":
                print("Saliendo del programa...")
                break
        case other:
            no_valido()