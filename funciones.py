def menu():
    menu=("Menu\n1.Listar la información\n2.Contar la información\n3.Buscar o filtrar información\n4.Buscar información relacionada\n5.Ejercicio Libre\n6.Salir")
    return(menu)

def ListarInformacion(datos):
    nombre=[]
    direccion=[]
    horario=[]
    informacion=[]
    for info in datos["directorios"]["directorio"]:
        nombre.append(info["nombre"]["content"])
        direccion.append(info["direccion"][1]["content"])
        horario.append(info["horario"])
    for infor in zip(nombre,direccion,horario):
        informacion.append(infor)
    return informacion

def ContarFarmacias(datos):
    farmacias=[]
    for farm in datos["directorios"]["directorio"]:
        farmacias.append(farm)
    return len(farmacias)

def BuscarFarmacias(localidad,datos):
    try:
        for farm in datos["directorios"]["directorio"]:
            if farm["direccion"][1]["content"]==localidad:
                print("\nEl nombre de la farmacia en esa dirección es: ")
                farmacia=farm["nombre"]["content"]
        return farmacia
    except:
        return "\nNo se ha encontrado ninguna farmacia en esa dirección."

def BuscarFarmaciasRelacionadasTelefono(telefono,datos):
    farmacias=[]
    for farm in datos["directorios"]["directorio"]:
        if farm["telefono"]["content"]==telefono:
            farmacias.append(farm["nombre"]["content"])
    return farmacias

def BuscarFarmaciasRelacionadasCorreo(correo,datos):    
    farmacias=[]
    for farma in datos["directorios"]["directorio"]:
        if farma["correo-electronico"]==correo:
            farmacias.append(farma["nombre"]["content"])
    return farmacias