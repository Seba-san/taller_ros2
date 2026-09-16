# generar_archivo.py
"""
Generador del archivo de claves para el Ejercicio 0 (Taller ROS 2).

Cómo usar este script:
Este programa encripta los datos utilizando la operación lógica XOR, 
donde la clave predeterminada es 37 (puede cambiarse). Gracias a las 
propiedades de XOR, la misma función sirve tanto para encriptar como 
para desencriptar.

El resultado final se guarda en el archivo local llamado 'archivo'.
(TODO: Faltaría implementar la comprobación mediante un checksum o un 
hash del original con el reconstruido para asegurar la integridad total).

En general, el formato del texto plano (antes de encriptar) es:
clave1 resultado1 clave2 resultado2 ...

Además, el archivo está separado en líneas, donde cada línea representa 
la lógica de un paso distinto dentro del ejercicio de ROS 2:
 - Línea 0 (Paso 0): Bolsa de códigos iniciales disponibles (Números enteros).
 - Línea 1 (Paso 1): Relación [Entero -> Float].
 - Línea 2 (Paso 2): Relación [Float -> Palabra temática de ROS/Robótica].
 - Línea 3 (Paso 3): Relación [Palabra temática -> Clave del alfabeto radiofónico].
 
Nota: Se generan 50 caminos únicos para que cada alumno tenga 
una clave final distinta (Ej: Alfa-Tango, Bravo-Charlie).
"""

import random
import itertools

def aplicar_xor(texto):
    return "".join(chr(ord(c) ^ 37) for c in texto)

# 50 palabras únicas, temáticas de Robótica, ROS y Espacio para el Paso 3
palabras_paso_3 = [
    "boxturtle", "cturtle", "diamondback", "electric", "fuerte", 
    "groovy", "hydro", "indigo", "jade", "kinetic", 
    "lunar", "melodic", "noetic", "ardent", "bouncy", 
    "crystal", "dashing", "eloquent", "foxy", "galactic", 
    "humble", "iron", "jazzy", "kilted", "kuka", 
    "fanuc", "abb", "yaskawa", "boston", "irobot", 
    "clearpath", "dji", "universal", "nvidia", "intel", 
    "arduino", "raspberry", "esp32", "orion", "apollo", 
    "voyager", "cassini", "hubble", "webb", "sputnik", 
    "soyuz", "perseverance", "curiosity", "spirit", "opportunity"
]

# Alfabeto radiotelefónico internacional (26 palabras)
alfabeto_fonetico = [
    "Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", 
    "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", 
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", 
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"
]

# Generamos permutaciones de dos palabras (ej: 'Alfa-Bravo', 'Charlie-Delta')
# Esto nos da más de 600 opciones únicas.
combinaciones_foneticas = [f"{w1}-{w2}" for w1, w2 in itertools.permutations(alfabeto_fonetico, 2)]

# Elegimos 50 al azar. (La semilla hace que siempre se elijan las mismas 50 si se ejecuta de nuevo)
random.seed(42)
claves_finales = random.sample(combinaciones_foneticas, 50)

# Generamos 50 números flotantes asegurándonos de que NO terminen en '0'.
p2_list = []
val = 10.11
while len(p2_list) < 50:
    s_val = str(round(val, 2))
    if not s_val.endswith('0'):
        p2_list.append(s_val)
    val += 0.01

# Construimos los 50 caminos
caminos = []
for i in range(50):
    p1 = str(10 + i)                 # Enteros: 10, 11, 12 ... 59
    p2 = p2_list[i]                  # Flotantes: 10.11, 10.12, 10.13 ...
    p3 = palabras_paso_3[i]          # Palabras temáticas
    p4 = claves_finales[i]           # Clave final fonética (Ej: Tango-Charlie)
    
    caminos.append((p1, p2, p3, p4))

# Armamos las líneas según la lógica del juego
linea_0 = [] # Bolsa inicial (Enteros)
linea_1 = [] # Parejas (Entero -> Float)
linea_2 = [] # Parejas (Float -> Palabra)
linea_3 = [] # Parejas (Palabra -> Clave)

for p1, p2, p3, p4 in caminos:
    linea_0.append(p1)
    
    linea_1.extend([p1, p2])
    linea_2.extend([p2, p3])
    linea_3.extend([p3, p4])

# Unimos los elementos con espacios
l0 = " ".join(linea_0)
l1 = " ".join(linea_1)
l2 = " ".join(linea_2)
l3 = " ".join(linea_3)

# Unimos las líneas con saltos de línea (que al encriptar se volverán '/')
texto_plano = f"{l0}\n{l1}\n{l2}\n{l3}"

# Encriptamos con XOR 37
texto_encriptado = aplicar_xor(texto_plano)

# Guardamos el archivo
with open('archivo', 'w') as f:
    f.write(texto_encriptado)

print(f"¡Se generó exitosamente el archivo 'archivo' encriptado")
