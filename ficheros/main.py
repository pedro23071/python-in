""" Los modos comunes para abrir archivos son:

"r": Lectura (modo por defecto). Da error si el archivo no existe.
"w": Escritura. Crea un archivo nuevo o sobrescribe uno existente.
"a": Añadir. Agrega contenido al final del archivo sin eliminar el contenido existente.
"r+": Lectura y escritura. """



from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + "\\ficheros\\mi_archivo.txt"

with open(ruta, "r") as archivo:
    # archivo.read()
    # archivo.write("texto insertado desde python \n")
    # print(archivo.read())
    print(archivo.readlines())