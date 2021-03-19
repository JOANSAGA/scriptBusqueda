import os
import shutil
import json

contenedor = os.getcwd()
salir = False
opcion = 0

def cargarArhivos():
    try:
        busqueda = open(str(contenedor) + '\\' + 'busqueda.txt', 'r')
        print("* busqueda.txt cargado.")
    except:
        print("* busqueda.txt no se encuentra.")
        file = open(str(contenedor) + '\\' + 'busqueda.txt', 'w')
        file.close()
        # crea el archivo de busquedas
        print("* busqueda.txt creado.")
        busqueda = open(str(contenedor) + '\\' + 'busqueda.txt', 'r')

    try:
        config = open(str(contenedor) + '\\' + 'config.json', 'r')
        print("* config.json cargado.")
        with config as file:
            data = json.load(file)
            if data == "":
                raise ValueError("Archivo vacio")
        
    except:
        print("* config.json no se encuentra.")
        data = {}
        data['directorios'] = []
        data['directorios'].append({
            'nombre': 'contenedor',
            'ruta': contenedor})
        with open(str(contenedor) + '\\' + 'config.json', 'w') as file:
            json.dump(data, file, indent=4)
            # crea el archivo de configuraciones
            print("* Archivo config.json creado.")
    config = str(contenedor) + '\\' + 'config.json'
    busqueda = str(contenedor) + '\\' + 'busqueda.txt'
    return busqueda,config

def linea():
    print("****************************************************************************")

def pedirNumEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("* Ingresa una opcion: "))
            correcto = True
        except ValueError:
            print('* Error, Ingresa un numero')
    return num

def seleccionarDirectorios(config):
    os.system('cls')
    linea()
    print("*           SELECCIONAR DIRECTORIOS DE BUSQUEDA:")
    cont = 1
    direc = False
    dirOpcion = []
    with open(config, 'r+') as file:
        data = json.load(file)
    for ruta in data['directorios']:
        print("* Opcion",cont,":")
        print("* Nombre: ", ruta['nombre'])
        print("* Ruta:   ", ruta['ruta'])
        linea()
        cont = cont + 1
        direc = True
    if direc != True:
        print("* No se encontraron directorios, agrege un directorio")
        os.system('pause')
        addModDirectorio(config)
    else:
        add = False
        while not add:
            num = pedirNumEntero()
            if num < cont:
                dirOpcion.append(num)
                dirOpcion = sorted(set(dirOpcion))
                print("* Directorios a buscar: ", dirOpcion)
                respVal= False
                while not respVal:
                    resp = input("* Desea agregar mas directorios a la busqueda? [s = si / n = no]: ")
                    if resp == "s" or resp == "S":
                        respVal = True
                    elif resp == "n" or resp == "N":
                        respVal = True
                        add = True
                    else:
                        print("* Opcion no valida escoja [s = si / n = no]")
            else:
                print("* Opcion no valida, agrege un numero de directorio")
            
    return dirOpcion

def validarDirectorio(directorio):
    
    isdir = os.path.isdir(directorio)
    if isdir:
        msg = "* Es un direcctorio valido"
    else:
        msg = "* Direcctorio no valido o no tiene acceso"
    return isdir, msg

def addModDirectorio(config):
    salir = False
    os.system('cls')
    while not salir:
        linea()
        print("*           DIRECTORIOS DE BUSQUEDA:")
        print("* Opcion 1: Agregar nuevo")
        print("* Opcion 2: Eliminar directorio")
        print("* Opcion 0: salir")
        linea()

        opcion = pedirNumEntero()

        if opcion == 1:
            os.system('cls')
            linea()
            directorioValido = False
            print("*           NUEVO DIRECTORIO DE BUSQUEDA:")
            nombre = input("* Ingresa un nombre para el directorio: ")
            while not directorioValido:
                directorio = input("* Ingresa el directorio: ")
                directorioValido, msg = validarDirectorio(directorio)
                print(msg)

            with open(config, 'r+') as file:
                data = json.load(file)
            data['directorios'].append({'nombre': nombre,'ruta': directorio})
            with open(config, 'r+') as file:
                json.dump(data, file, indent=4)
                print("* Directorio creado")
                linea()
                os.system('pause')
        elif opcion == 2:
            os.system('cls')
            linea()
            print("*           ELIMINAR DIRECTORIO DE BUSQUEDA:")
            cont = 1
            direc = False
            with open(config, 'r+') as file:
                data = json.load(file)
                
                for ruta in data['directorios']:
                    print("* Opcion",cont,":")
                    print("* Nombre: ", ruta['nombre'])
                    print("* Ruta:   ", ruta['ruta'])
                    linea()
                    cont = cont + 1
                    direc = True            
                if direc == True:
                    dirOpcion = pedirNumEntero()
                    if dirOpcion <= cont:
                        with open(config, 'w') as file:
                            data['directorios'].pop(dirOpcion - 1)
                            json.dump(data, file, indent=4)
                    else:
                        print("* Opcion no valida")
                else:
                    print("* No hay directorios que mostrar")
                    print("* Debe agregar un nuevo directorio")
        elif opcion == 0:
            os.system("cls")
            salir = True
        else:
            print("* Introduce una opcion valida")
            os.system("pause")
            os.system("cls")

def BuscaNum(dirBusqueda, config, busqueda):
    print(dirBusqueda)
    print(config)
    print(busqueda)
    cont = 1
    with open(config, 'r') as file:
        data = json.load(file)

os.system("cls")
linea()
busqueda,config = cargarArhivos()
while not salir:
    linea()
    print("*           MENU PRINCIPAL:")
    print("* Opcion 1: Busqueda por numero")
    print("* Opcion 2: Busqueda por numero y fecha")
    print("* Opcion 3: Agregar o Modificar directorios de busqueda")
    print("* Opcion 0: salir")
    linea()

    opcion = pedirNumEntero()

    if opcion == 1:
        dirBusqueda = seleccionarDirectorios(config)
        BuscaNum(dirBusqueda, config, busqueda)
    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        addModDirectorio(config)
    elif opcion == 0:
        salir = True
    else:
        print("* Introduce una opcion valida")
        os.system("pause")
        os.system("cls")
