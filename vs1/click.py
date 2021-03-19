import os
import shutil

# 247-1 
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones247 julio-diciembre2019"
# 247-2 
path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones247-enero-junio2020"
# 250 
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\grabaciones250 septiembre2019-noviembre2019\2020"
# cloud 
#path = r"\\DESKTOP-UMULP95\disco duro grabaciones\GRABACIONES\DINOMI EN LA NUBE"

dir2 = r"C:\Users\SINERGIA\Desktop\script\vs1"


archivo = open(str(dir2) + '\\' +
               'busqueda.txt', 'r')

with archivo as busqueda:
    for numero in busqueda:
        numero = str(numero).rstrip()
        print("*********ANALIZANDO numero: " + str(numero) + "*********")
        with os.scandir(path) as meses:
            for mes in meses:
                if mes.is_dir():
                    print("**********ANALIZANDO MES: " +
                          str(mes) + "**********")
                    with os.scandir(mes) as dias:
                        for dia in dias:
                            if dia.is_dir():
                                print("Analizando dia: " + str(dia))
                                with os.scandir(dia) as ficheros:
                                    # if "07" not in mes.name and "31" not in mes.name:
                                    for fichero in ficheros:
                                        if fichero.is_file():
                                            if numero in fichero.name:
                                                print(
                                                    "archivo encontrado: " + fichero.name)
                                                # cambiar path al directorio escogido
                                                newDir = str(
                                                    dir2) + "\\" + numero
                                                try:
                                                    os.stat(newDir)
                                                    print(
                                                        "Directorio existe: " + newDir)
                                                except:
                                                    os.mkdir(newDir)
                                                    print(
                                                        "Directorio creado: " + newDir)
                                                shutil.copy(
                                                    fichero.path, newDir)
os.system('pause')
