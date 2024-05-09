
# Ejercicio ROS2 - Publicación y Suscripción de Topics

Este repositorio contiene un ejercicio práctico para familiarizarse con ROS2, especialmente enfocado en la publicación y suscripción de topics utilizando la terminal.

## Estructura del Repositorio

El repositorio contiene el siguiente archivo esencial para el ejercicio:
- `ej0.py`: Script de Python que inicia nodos y topics en ROS2.

## Instrucciones de Uso

### Iniciar el Nodo

1. Abre una terminal y navega al directorio donde se encuentra el archivo `ej0.py`.
2. Ejecuta el script utilizando Python3:
   ```bash
   python3 ej0.py
   ```
Si esta todo bien, deberia salir el siguiente mensaje:
 ```bash
   [INFO] [1715213981.151778017] [Desencriptador]: Iniciando el ejercicio 0. Para comenzar debes publicar en el topic correcto tu nombre en minusculas.
   ```

### Suscribirse a un Topic

3. Abre una nueva terminal y suscríbete al topic `/respuesta` para ver las respuestas que genera el script:
   ```bash
   ros2 topic echo /respuesta
   ```

### Publicar en Topics

4. Abre otra terminal adicional para listar todos los topics disponibles:
   ```bash
   ros2 topic list
   ```
   Deberías ver una lista de topics como `tu_nombre`, `paso_1`, `paso_2`, etc.

5. Basándote en la información del topic `/respuesta` y la lista de topics, comienza a publicar en cada uno siguiendo el orden indicado. Puedes utilizar el comando `ros2 topic pub`. Por ejemplo, para publicar en el topic `tu_nombre`:
   ```bash
   ros2 topic pub -t 1 /tu_nombre_paso_0 std_msgs/msg/String data:\ "tu nombre"\ 
   ```

   Repite este paso para cada uno de los topics listados, ajustando el tipo de dato y el contenido según corresponda. Utilice el autocompletar con la tecla <tab>

## Objetivo del Ejercicio

El objetivo es practicar la publicación y suscripción de diferentes tipos de datos en ROS2, así como mejorar la familiarización con el uso de comandos en la terminal. Este ejercicio también te ayudará a entender cómo fluyen los datos a través de los topics en un sistema ROS2.

## Soporte

Si encuentras algún problema o tienes alguna pregunta acerca de este ejercicio, por favor crea una issue en este repositorio.

---

Esperamos que encuentres este ejercicio útil y educativo para tu aprendizaje de ROS2.
