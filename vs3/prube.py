import os
import shutil

directorio = "\\\\nas.sng.com\\Public\\Grabaciones\\SERVIDOR 250" + "\\2021\\01\\04"
with os.scandir(directorio) as ficheros:
    for fichero in ficheros:
        print(fichero)