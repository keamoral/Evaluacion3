import os
os.system("cls")

menu="""
1.Registrar vehiculo
2.Listar todos los vehiculos registrados
3.Imprimir orden de reparacion
4.Salir del programa
"""
vehiculos=[]

titulo="""        Registros vehiculo
----------------------------------------------------
|   Marca   |  Año Fabricacion  |  Kilometraje  |  Costo de reparacion  |   Impuesto de Servicio Calculado  |  Costo total a pagar  |
"""
marca=["toyota","ford","chevrolett"]

def REGISTRAR_VEHICULO():
    while True:
        try:
            Marca=input(f"Marca{marca}: ")
            AñoFabr=int(input("Año de fabricacion: "))
            Kilometraje=int(input("Kilometraje: "))
            Costo_reparacion=int(input("Costo de reparacion(pesos): "))
            Impuesto_servicio= round(Costo_reparacion* 0.08)
            Total_pagar=(Costo_reparacion + Impuesto_servicio)
            vehiculos.append([Marca,AñoFabr,Kilometraje,Costo_reparacion,Impuesto_servicio,Costo_reparacion])
            input("Vehiculo Registrado con exito!")
            return
        except Exception as e:
            input(f"Excepcion de registro en:{str(e)}")

def LISTAR_TODOS():
    salida=titulo
    for t in vehiculos:
        salida+= f"{t[0]:10s}"#Marca
        salida+= f"{t[1]:15d}"#Año
        salida+= f"{t[2]:15d}"#Kilometraje
        salida+= f"{t[3]:30d}"#Costo reparacion
        salida+= f"{t[4]:30d}"#Impuesto servicio
        salida+= f"{t[5]:20d}"#Total a pagar
        salida+= f"\n"
    return salida

def LISTAR_MARCA(marca):
    salida=titulo
    for t in vehiculos:
        if t[0]:
            salida+= f"{t[0]:10s}"#Marca
            salida+= f"{t[1]:15d}"#Año
            salida+= f"{t[2]:15d}"#Kilometraje
            salida+= f"{t[3]:30d}"#Costo reparacion
            salida+= f"{t[4]:30d}"#Impuesto servicio
            salida+= f"{t[5]:20d}"#Total a pagar
            salida+= f"\n"
    return salida


def IMPRIMIR_ORDEN():
    m=input(f"Desea imprimir [todo/{marca}]: ")
    if m == "todo":
        with open (f"Ordenes totales.txt","w", encoding="utf-8") as archivo:
            archivo.write(LISTAR_TODOS())
    elif m== m:
        with open (f"Ordenes de {m}.txt","w",encoding="utf-8") as archivo:
            archivo.write(LISTAR_MARCA(marca))
    


    

#main
while True:
    try:
        opc=int(input(menu))
        if opc==4:
            input("Gracias por usar nuestro programa")
            break
        if opc==1:
            REGISTRAR_VEHICULO()
        elif opc==2:
            print(LISTAR_TODOS())
        elif opc==3:
            IMPRIMIR_ORDEN()
        else:
            input("Opcion no valida")
    except Exception as e:
        input(f"Excepcion en menu:{str(e)}")