import json
from funciones import *

with open('proyecto.json', encoding='utf-8') as fichero:
    datos=json.load(fichero)
print(menu())
opcion=int(input("Elige una opción: "))

while opcion!=6:
    
    if opcion==1:
        for info in ListarInformacion(datos):
            print(f"El nombre de la farmacia es {info[0]}, se encuentra en {info[1]} y su horario es {info[2]}")
        opcion=int(input("\nElige una opción: "))
    
    elif opcion==2:
        print(f"El número de registros de farmacias que se dispone es de {ContarFarmacias(datos)} ")
        opcion=int(input("\nElige una opción: "))
    
    elif opcion==3:
        direccion=input("Introduce una direccion: ")
        farmacia=BuscarFarmacias(direccion,datos)
        print(farmacia)
        opcion=int(input("\nElige una opción: "))
    
    elif opcion==4:
        print("1. Búsqueda por correo electrónico.\n2. Búsqueda por número de teléfono.")
        busqueda=int(input("Elige una opción: "))
        if busqueda==1:
            correo=input("Introduce el correo electrónico de la farmacia que desees buscar: ")
            for info in BuscarFarmaciasRelacionadasCorreo(correo,datos):
                print(info)
            opcion=int(input("\nElige una opción: "))
        elif busqueda==2:
            telefono=input("Introduce el número de teléfono de la farmacia que desees buscar: ")
            for info in BuscarFarmaciasRelacionadasTelefono(telefono,datos):
                print(info)
            opcion=int(input("\nElige una opción: "))

    elif opcion==5:
        print("Para una búsqueda más precisa intenta poner el nombre más exacto posible.")
        nombre=input("Introduce el nombre de la farmacia que deseas buscar: ")
        for info in EjercicioLibre(nombre,datos):
            print(f"Los datos de contacto de la farmacia son {info[0]} y su número es {info[1]}, su horario es {info[2]} y su localización en OSM es: \n{info[3]}")
        opcion=int(input("\nElige una opción: "))