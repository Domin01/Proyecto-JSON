import json
from funcionesjson import *

with open('proyecto.json', encoding='utf-8') as fichero:
    datos=json.load(fichero)
print(menu())
opcion=int(input("Elige una opción: "))

while opcion!=6:
    
    if opcion==1:
        print("El nombre de las farmacias son: \n")
        for info in ListarInformacion(datos):
            print(info)
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