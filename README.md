# Taller de ROS2 - JAR2026

Este repositorio contiene todos los materiales y recursos utilizados durante el Taller de ROS2 que se llevará a cabo del 3 al 6 de noviembre de 2026, en el marco de la Jornadas Argentinas de Robótica (JAR2026). El taller estuvo diseñado para introducir a los participantes en los fundamentos y herramientas avanzadas de ROS2, cubriendo temas como topics, servicios, TF2, la integración con sistemas de simulación, entre otros.

## Contenidos del Repositorio

En este repositorio encontrarás los siguientes recursos:

- **Slides**: Presentaciones utilizadas durante cada sesión del taller.
- **Códigos de Ejemplo**: Scripts y proyectos de ejemplo que demuestran el uso práctico de ROS2 en diferentes contextos y aplicaciones.
- **Ejercicios**: Actividades prácticas diseñadas para reforzar el aprendizaje de los conceptos presentados.
- **Soluciones a Ejercicios**: Soluciones propuestas a los ejercicios planteados durante el taller.



## Links de las Slides:
- [**Clase 0**](https://docs.google.com/presentation/d/1yP94nGcVkkpUEM_PgunxwUG_UKHOs50bu4yO9WQafQ8/edit?usp=sharing)
- [**Clase 1**](https://docs.google.com/presentation/d/1WK-VeUPZ32vCandjKE6lsq8uTf7t1sVb5cad8IlsJwA/edit?usp=sharing)
- [**Clase 2**](https://docs.google.com/presentation/d/1ntkEgVn08wdpLrAHdVX2MWw4HIsRUO5cztb4QlpaVnM/edit?usp=sharing)
- [**Clase 3**](https://docs.google.com/presentation/d/1isvk3wXXPuZOWqGAUEkuBf6QzFRDo9SW3Fe_Sh8flbw/edit?usp=sharing)



## Cómo Usar Este Repositorio

Para hacer uso de los materiales y ejemplos proporcionados en este repositorio, te recomendamos clonar o descargar todo el repositorio a tu sistema local.
Para esto realizar:
```bash
git clone https://github.com/Seba-san/taller_ros2.git
```
Si quieres utilizar el contenedor de docker, primero debes instalarlo siguiendo el procedimiento descripto [AQUÍ](https://docs.docker.com/engine/install/).

Luego para compilar el contenedor hacer:
```bash
cd taller_ros2/docker
docker build -t jar2026 -f Dockerfile .
```

Para finalizar y para comprobar el funcionamiento hacer:
```bash
cd taller_ros2/docker
./run jar2026
./entrar
gz sim
```
Si abre el simulador Gazebo, quiere decir que todo funciona correctamente.


## Ediciones anteriores
Puedes consultar todo el material, código y recursos de la primera edición del taller (JAR 2024) accediendo directamente a su rama correspondiente:
- [**Material completo de la Edición 1**](https://github.com/Seba-san/taller_ros2/tree/edicion1)

### Datos de la Encuesta

Al finalizar el taller anterior, se realizó una encuesta de satisfacción para recoger las impresiones y el feedback de los participantes. Los datos recogidos han sido analizados y están disponibles para consulta:

- [Datos de la Encuesta y Gráficos (Edición 1)](https://github.com/Seba-san/taller_ros2/tree/edicion1/encuesta_ed1)

En esta carpeta, encontrarás tanto el archivo CSV con las respuestas de la encuesta como varias imágenes con gráficos que resumen visualmente la información recogida.

### Fotos del Evento

Durante el desarrollo del taller se tomaron varias fotos que capturan momentos clave del evento y la participación activa de los asistentes. Estas fotos están disponibles en la siguiente carpeta:

- [Fotos del Taller (Edición 1)](https://github.com/Seba-san/taller_ros2/tree/edicion1/fotos)


## Contribuciones y Feedback

Si deseas contribuir a este repositorio o tienes sugerencias para mejorar los materiales del taller, no dudes en abrir un issue o realizar un pull request. Tu feedback es invaluable para mejorar futuras ediciones del taller.

## Contacto

Si tienes preguntas específicas sobre el taller o necesitas más información, puedes entrar al canal de [Discord](https://discord.gg/ppyX5qg6aX).

¡Gracias por participar en el Taller de ROS2 en la JAR2026!



