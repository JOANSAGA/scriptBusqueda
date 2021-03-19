import os
import shutil

# 247-1
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones247 julio-diciembre2019"
# 247-2
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones247-enero-junio2020"
# 250 2020
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones250 septiembre2019-noviembre2019\2020"
# 250 2019
path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones250 septiembre2019-noviembre2019\2019"
# cloud
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\DINOMI EN LA NUBE"

dir1 = path
dir2 = r"C:\Users\SINERGIA\Desktop\script\vs2"
cont = 0
cont2 = 0

try:
    archivo = open(str(dir2) + '\\' + 'busqueda.txt', 'r')
    print("*********************** ARCHIVO busqueda.txt CARGADO...")
except:
    print("Archivo busqueda.txt no se encontra")
    os.system("pause")

with archivo as lineas:
    for parametros in lineas:
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
        #print("numero: " + str(numero))
        #print("fecha: " + str(fechaUnida))
        #print("año: " + str(year) + " mes: " + str(mes) + " dia: " + str(dia))
        #print("hora: " + str(hora))

        directorio = str(dir1) + '\\' + str(mes) + '\\' + str(dia)
        print("*********************** ANALIZANDO MES: " + mes + " DIA: " + dia)
        print("*********************** ANALIZANDO RUTA: ")
        print("*********************** " + str(directorio))
        print("*********************** BUSCANDO POR NUMERO: " + numero)
        cont = 0
        with os.scandir(directorio) as ficheros:
            for fichero in ficheros:
                #print(numero + "//////" + fichero.name)
                if fichero.is_file():
                    if numero in fichero.name:
                        cont = cont + 1
                        newDir = str(dir2) + "\\" + numero
                        try:
                            os.stat(newDir)
                            if cont <= 1:
                                print(
                                    "*********************** DIRECCTORIO EXISTE: " + newDir)
                        except:
                            os.mkdir(newDir)
                            if cont <= 1:
                                print(
                                    "*********************** DIRECCTORIO CREADO: " + newDir)
                        shutil.copy(fichero.path, newDir)
        print("*********************** ARCHIVOS ENCONTRADOS: " + str(cont))
        print("*********************** BUSCANDO POR FECHA: " + fechaUnida)
        with os.scandir(directorio) as ficheros:
            for fichero in ficheros:
                #print(fechaUnida + "//////" + fichero.name)
                if fichero.is_file():
                    if fechaUnida in fichero.name:
                        cont = cont + 1
                        newDir = str(dir2) + "\\" + numero
                        try:
                            os.stat(newDir)
                        except:
                            os.mkdir(newDir)
                        newDir = str(dir2) + "\\" + numero + "\\" + fechaUnida
                        try:
                            os.stat(newDir)
                            if cont <= 1:
                                print(
                                    "*********************** DIRECCTORIO EXISTE: " + newDir)
                        except:
                            os.mkdir(newDir)
                            if cont <= 1:
                                print(
                                    "*********************** DIRECCTORIO CREADO: " + newDir)
                        shutil.copy(fichero.path, newDir)
        print("*********************** ARCHIVOS ENCONTRADOS: " + str(cont))
os.system('pause')
