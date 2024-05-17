# Ejercicio ROS2 - Navegación de Laberintos con Turtlebot3

## Descripción

Este ejercicio está diseñado para que te familiarices con las habilidades básicas de programación en ROS2, incluyendo la creación de nodos, la suscripción a topics y la publicación en ellos.

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
   Asegúrate de configurar la variable `Fixed_frame` a `base_link` y ajusta los demás parámetros según sea necesario para visualizar correctamente la simulación.

4. Si deseas controlar manualmente el robot dentro del laberinto, usa el nodo de teleoperación:
    ```bash
    ros2 run turtlebot3_teleop teleop_keyboard
    ```

## Objetivos del Ejercicio

- **Desarrollar un Nodo**: Crea un nodo que publique los comandos de velocidad para el robot, de manera que se mueva más rápido y complete el laberinto lo antes posible. También puedes incorporar un sistema que detenga automáticamente el vehículo cuando haya un obstáculo lo suficientemente cerca. El actual récord está en 1 minuto, ¿podrás mejorarlo?

### Ideas de Resolución

- Tomar el mensaje que publica `teleop_keyboard`, modificarlo y publicarlo nuevamente. Para esto, necesitas que `teleop_keyboard` publique en otro topic que no sea `/cmd_vel`. Una forma de hacer esto es usando remapeo de topics:
    ```bash
    ros2 run turtlebot3_teleop teleop_keyboard --ros-args -r cmd_vel:=custom_cmd_vel
    ```
- Otra forma es modificando el programa de teleop. Para esto, se requiere descargar el código desde el repositorio:
    ```bash
    wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/ros2/turtlebot3_teleop/turtlebot3_teleop/script/teleop_keyboard.py
    ```
   y modificar todo lo que sea necesario.

## Recursos Adicionales

- [Tutorial ROS2](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)
- [Documentación de Turtlebot3](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

## Soporte

Si encuentras algún problema o tienes alguna pregunta acerca de este ejercicio, por favor crea una issue en el repositorio de GitHub del curso.

---

¡Esperamos que este ejercicio sea un reto divertido y educativo que te ayude a mejorar tus habilidades con ROS2!
