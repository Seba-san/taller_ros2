# Ejercicio ROS2 - Navegación de Laberintos con Turtlebot3

## Descripción
Este ejercicio está diseñado para que te familiarices con las habilidades básicas de programación en ROS2, incluyendo la creación de nodos, la subscripción a topics y la publicación en ellos. 

El escenario del ejercicio implica un laberinto en el cual se encuentra un robot Turtlebot3. Tu tarea es desarrollar un nodo que permita al robot navegar y salir del laberinto de manera eficiente. Cada vez que reinicies el simulador, se generará un nuevo diseño de laberinto, lo cual añade un desafío adicional al ejercicio.


## Instrucciones de Uso

1. Abre una terminal y navega a la carpeta donde se encuentra el archivo de lanzamiento:
    ```bash
    cd /root/catkin_ws/volumen
    ```

2. Inicia la simulación del laberinto ejecutando:
    ```bash
    ros2 launch lanzar_laberinto.py
    ```

3. En otra terminal, abre Rviz2 para visualizar el entorno y la navegación del robot:
    ```bash
    ros2 run rviz2 rviz2
    ```
   Asegúrate de configurar la variable "Fixed_frame" a "base_link" y ajusta los demás parámetros según sea necesario para visualizar correctamente la simulación.

4. Si deseas controlar manualmente el robot dentro del laberinto, usa el nodo de teleoperación:
    ```bash
    ros2 run turtlebot3_teleop teleop_keyboard
    ```

## Objetivos del Ejercicio

- **Desarrollar un Nodo**: Crea un nodo en ROS2 que pueda suscribirse al topic que proporciona información del sensor del robot y publicar comandos de movimiento.

## Recursos Adicionales

- [Tutorial ROS2](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)
- [Documentación de Turtlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

## Soporte

Si encuentras algún problema o tienes alguna pregunta acerca de este ejercicio, por favor crea una issue en el repositorio de GitHub del curso.

---

¡Esperamos que este ejercicio sea un reto divertido y educativo que te ayude a mejorar tus habilidades con ROS2!
