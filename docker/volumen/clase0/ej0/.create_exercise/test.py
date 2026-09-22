"""
Como usar este script:
encripta usando la operacion xor, donde la clave es 37, pero puede cambiar. Con la misma funcion se encripta y se desencripta. 
El resultado se guarda en el ruta_archivo_encriptado y para comprobar el buen funcionamiento, se lee ese archivo y se desencripta nuevamente. 
Faltaria comprobar un checksum o un hash, del original con el reconstruido.

En general el formato del archivo es:
clave resultado clave2 resultado2

ademas esta separado en lineas, donde cada linea es un paso dentro del ejericio
"""

import os

# Definimos la ruta de los archivos para simular el guardado y la lectura
ruta_archivo_original = 'archivod'
ruta_archivo_encriptado = 'archivo'
ruta_archivo_desencriptado = 'archivod2'


def cifrar_descifrar(texto):
    pss=37 # Clave!
    dd="".join(chr(ord(c) ^ pss) for c in texto)
    return dd



# Leer el archivo original
with open(ruta_archivo_original, 'r') as file:
    texto_a_cifrar = file.read()

# Cifrar el texto
texto_cifrado = cifrar_descifrar(texto_a_cifrar)

# Guardar el texto cifrado en archivo encriptado
with open(ruta_archivo_encriptado, 'wb') as file:
    file.write(texto_cifrado.encode('utf-8'))

# Leer el archivo cifrado
with open(ruta_archivo_encriptado, 'rb') as file:
    texto_cifrado_leido = file.read().decode('utf-8')

# Descifrar el texto
texto_descifrado = cifrar_descifrar(texto_cifrado_leido)

# Guardar el texto descifrado en un archivo (opcional, solo para verificación)
with open(ruta_archivo_desencriptado, 'w') as file:
    file.write(texto_descifrado)

print(texto_descifrado)

