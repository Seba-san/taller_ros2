# Workshop ROS2 - Cronometraje en Laberinto

## Descripción

Este ejercicio forma parte de un workshop de ROS2, centrado en desarrollar y afinar tus habilidades para manejar la comunicación entre nodos en un entorno simulado. El objetivo es programar un robot para que navegue a través de un laberinto, monitorear su posición, y calcular el tiempo que tarda en completarlo, desde el envío del primer comando hasta que cruza la línea de meta.

## Instrucciones de Uso

1. Para desarrollar el código se aconseja testear su desempeño usando los datos grabados con rosbag. Para esto puedes ejecutarlo haciendo:
     ```bash
    cd ej2/
    ros2 bag play record
    ```
    Recuerda que puedes pausar y reanudar la reproducción con la tecla <space>. Para más información puedes hacer:
    ```bash    
    ros2 bag --help
    ```
2. Para medir el tiempo puedes usar los headers de los mensajes.

3. Para publicar log info en python se puede hacer:
   ```python    
    rclpy.self.get_logger().info('Mensaje')
    ```
    En el equivalente en c++ es:
    ```cpp    
    RCLCPP_INFO(this->get_logger(), "Mensaje");
    ```

4. Utiliza rosbag para grabar los datos del recorrido del robot. Esto te permitirá realizar pruebas repetitivas y mejorar el rendimiento del algoritmo:
    ```bash
    ros2 bag record -o [nombre_del_bagfile] /tf /cmd_vel
    ```

## Objetivos del Ejercicio

- **Leer la Posición del Robot**: Implementa un nodo que lea la posición actual del robot utilizando el topic TF.
- **Medir el Tiempo**: Calcula cuánto tiempo tarda el robot en completar el laberinto y publica el resultado usando `loginfo`.
- **Superar el Tiempo Record**: Intenta batir el tiempo record actual y graba el intento con rosbag.

## Recursos Adicionales

- [Tutorial de ROS2 TF](https://docs.ros.org/en/humble/Concepts/Intermediate/About-Tf2.html)
- [Documentación sobre rosbag](https://docs.ros.org/en/foxy/Tutorials/Ros2bag/Recording-And-Playing-Back-Data.html)
- [ROS2 Launch Files](https://docs.ros.org/en/foxy/Tutorials/Launch-system.html)

## Soporte

Si tienes preguntas o encuentras algún problema durante el ejercicio, no dudes en abrir una issue en el repositorio del workshop o contactar directamente a los organizadores.

---

¡Diviértete aprendiendo y desafiando tus habilidades con ROS2 en este ejercicio interactivo y técnico!
