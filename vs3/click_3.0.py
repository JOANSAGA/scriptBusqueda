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
    print("**********************************************************************")

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
    cont = 1
    dirOpcion = []
    archivobusqueda = busqueda

    os.system("cls")

    with open(config, 'r') as file:
        data = json.load(file)

    for ruta in data['directorios']:
        if cont in dirBusqueda:
            dirOpcion.append(ruta['ruta'])
        cont = cont + 1
    cont = 0
    for rutas in dirOpcion:
        with open(archivobusqueda, 'r') as busqueda:
            for numero in busqueda:
                parametros = numero.split()
                numero = parametros[0]
                linea()
                print("* Analizando numero: ", numero)
                print("* Analizando directorio: ", rutas)
                with os.scandir(rutas) as years:
                    for year in years:
                        if year.is_dir():
                            with os.scandir(year) as meses:
                                for mes in meses:
                                    if mes.is_dir():
                                        with os.scandir(mes) as dias:
                                            for dia in dias:
                                                if dia.is_dir():
                                                    os.system("cls")
                                                    linea()
                                                    print("* Ruta: ", rutas)
                                                    print("* Numero: ", numero)
                                                    print("* Año: ", year)
                                                    print("* Mes: ", mes)
                                                    print("* Dia: ", dia)
                                                    print("* Archivos encontrados: ", cont)
                                                    linea()
                                                    with os.scandir(dia) as ficheros:
                                                        for fichero in ficheros:
                                                            if fichero.is_file():
                                                                if numero in fichero.name:
                                                                    print("archivo encontrado: " + fichero.name)
                                                                    newDir = contenedor + "\\" + numero
                                                                    try:
                                                                        os.stat(newDir)
                                                                        print(
                                                                            "Directorio existe: " + newDir)
                                                                    except:
                                                                        os.mkdir(newDir)
                                                                        print(
                                                                            "Directorio creado: " + newDir)
                                                                    cont = cont + 1
                                                                    shutil.copy(fichero.path, newDir)

def BuscaNumFecha(dirBusqueda, config, busqueda):
    cont = 1
    dirOpcion = []
    archivobusqueda = busqueda

    os.system("cls")

    with open(config, 'r') as file:
        data = json.load(file)

    for ruta in data['directorios']:
        if cont in dirBusqueda:
            dirOpcion.append(ruta['ruta'])
        cont = cont + 1
    
    for rutas in dirOpcion:
        with open(archivobusqueda, 'r') as busqueda:
            for parametros in busqueda:
                cont = 0
                parametros = parametros.split()
                numero = parametros[0]
                fecha = parametros[1]
                fechaSeparda = [fecha[i:i+4] for i in range(0, len(fecha), 4)]
                year = fechaSeparda[0]
                fechaSeparda = fechaSeparda[1]
                mesDia = [fechaSeparda[i:i+2] for i in range(0, len(fechaSeparda), 2)]
                mes = mesDia[0]
                dia = mesDia[1]
                hora = parametros[2]
                fechaUnida = str(fecha) + "-" + str(hora)
                
                directorio = rutas + '\\' + str(year) + '\\' + str(mes) + '\\' + str(dia)
                #directorio = "\\\\nas.sng.com\\Public\\Grabaciones\\SERVIDOR 250\\2021\\01\\04"
                print(directorio)
                # os.system("cls")
                linea()
                print("* Ruta: ", rutas)
                print("* Numero: ", numero)
                print("* Año: ", year)
                print("* Mes: ", mes)
                print("* Dia: ", dia)
                print("* Archivos encontrados: ", cont)
                linea()
                try:
                    with os.scandir(directorio) as ficheros:
                        for fichero in ficheros:
                            #print(numero + "//////" + fichero.name)
                            if fichero.is_file():
                                if numero in fichero.name:
                                    cont = cont + 1
                                    newDir = str(contenedor) + "\\" + numero
                                try:
                                    os.stat(newDir)
                                    if cont <= 1:
                                        print("* DIRECCTORIO EXISTE: " + newDir)
                                except:
                                    os.mkdir(newDir)
                                    if cont <= 1:
                                        print("* DIRECCTORIO CREADO: " + newDir)
                                shutil.copy(fichero.path, newDir)
                    with os.scandir(directorio) as ficheros:
                        for fichero in ficheros:
                            #print(fechaUnida + "//////" + fichero.name)
                            if fichero.is_file():
                                if fechaUnida in fichero.name:
                                    cont = cont + 1
                                    newDir = str(contenedor) + "\\" + numero
                                    try:
                                        os.stat(newDir)
                                    except:
                                        os.mkdir(newDir)
                                    newDir = str(contenedor) + "\\" + numero + "\\" + fechaUnida
                                    try:
                                        os.stat(newDir)
                                        if cont <= 1:
                                            print(
                                                "* DIRECCTORIO EXISTE: " + newDir)
                                    except:
                                        os.mkdir(newDir)
                                        if cont <= 1:
                                            print(
                                                "* DIRECCTORIO CREADO: " + newDir)
                                    shutil.copy(fichero.path, newDir)
                    os.system("pause")
                except:
                    print("* DIRECCTORIO NO EXISTE: ", directorio)
                    os.system("pause")

os.system("cls")
linea()
busqueda, config = cargarArhivos()
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
        dirBusqueda = seleccionarDirectorios(config)
        BuscaNumFecha(dirBusqueda, config, busqueda)
    elif opcion == 3:
        addModDirectorio(config)
    elif opcion == 0:
        salir = True
    else:
        print("* Introduce una opcion valida")
        os.system("pause")
        os.system("cls")

