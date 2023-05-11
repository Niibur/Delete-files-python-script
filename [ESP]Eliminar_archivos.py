import os
import time

def search_for_files(path, searched_file):
    """
    Esta función busca en el directorio especificado por el usuario el archivo con el nombre especificado.
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):        
        for file in filenames:
            if file == searched_file:
                files.append(os.path.join(dirpath, file))
    return files

def confirm_excluding(files):
    """
    Esta función permite al usuario confirmar si desea excluir los archivos encontrados.
    """
    num_files = len(files)
    print(f"> Se encontraron {num_files} archivo(s) con el nombre especificado.")
    if num_files == 0:
        return
    answer = input("> ¿Desea excluir los archivos? Escriba 'Si' para confirmar: ")
    if answer == "Si":
        num_excluded = 0
        for file in files:
            try:
                os.remove(file)
                num_excluded += 1
            except OSError as e:
                print(f"> No se pudo excluir el archivo {file}: {e}")
        print(f"> Se excluyeron {num_excluded} archivo(s).")

print('>>> Este programa busca archivos para borrar según su nombre.')
directory = input("> ¿Qué directorio desea escanear? ")
filename = input("> ¿Cuál es el nombre del archivo? ")

print(f"> Escaneando el directorio {directory} en busca de archivos con el nombre {filename}...")

start_time = time.time()
files = search_for_files(directory, filename)
elapsed_time = time.time() - start_time

if len(files) == 0:
    print(f"> No se encontraron archivos con el nombre {filename} en el directorio {directory}.")
else:
    confirm_excluding(files)
    
print(f"> El tiempo total de ejecución fue de {elapsed_time:.2f} segundos.")
