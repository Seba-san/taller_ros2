# Taller de ROS2 - JAR2024

Este repositorio contiene todos los materiales y recursos utilizados durante el Taller de ROS2 que se llevó a cabo del 4 al 7 de junio de 2024, en el marco de la Jornadas Argentinas de Robótica (JAR2024). El taller estuvo diseñado para introducir a los participantes en los fundamentos y herramientas avanzadas de ROS2, cubriendo temas como topics, servicios, TF2, la integración con sistemas de simulación, entre otros.

## Contenidos del Repositorio

En este repositorio encontrarás los siguientes recursos:

- **Slides**: Presentaciones utilizadas durante cada sesión del taller.
- **Códigos de Ejemplo**: Scripts y proyectos de ejemplo que demuestran el uso práctico de ROS2 en diferentes contextos y aplicaciones.
- **Ejercicios**: Actividades prácticas diseñadas para reforzar el aprendizaje de los conceptos presentados.
- **Soluciones a Ejercicios**: Soluciones propuestas a los ejercicios planteados durante el taller.

## Datos de la Encuesta

Al finalizar el taller, se realizó una encuesta de satisfacción para recoger las impresiones y el feedback de los participantes. Los datos recogidos han sido analizados y están disponibles para consulta:

- [Datos de la Encuesta y Gráficos](https://github.com/Seba-san/taller_ros2/tree/edicion1/encuesta_ed1)

En esta carpeta, encontrarás tanto el archivo CSV con las respuestas de la encuesta como varias imágenes con gráficos que resumen visualmente la información recogida.

## Links de las Slides:
- [**Clase 0**](https://docs.google.com/presentation/d/1k6obPYxbZB0H_htOwfBepzbnCYXe_RegUZhRNxZCZjI/edit?usp=sharing)
- [**Clase 1**](https://docs.google.com/presentation/d/11k9eBOFxvmiWe9NWASTNl7dkU7nx8e7zZ2jAD1ilfZk/edit?usp=sharing)
- [**Clase 2**](https://docs.google.com/presentation/d/1NKGI1dmCHBV7r093RLKvA4wBlRKUyxEHxCL658y7j3E/edit?usp=sharing)
- [**Clase 3**](https://docs.google.com/presentation/d/1uN_3U4GYV5XyYaNQwtQP2mVNK9dymGk9I5DRBKU6oSg/edit?usp=sharing)


## Fotos del Evento

Durante el desarrollo del taller se tomaron varias fotos que capturan momentos clave del evento y la participación activa de los asistentes. Estas fotos están disponibles en la siguiente carpeta:

- [Fotos del Taller](link-a-la-carpeta-de-fotos)

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
docker build -t jar2024 -f Dockerfile .
```

Para finalizar y para comprobar el funcionamiento hacer:
```bash
cd taller_ros2/docker
./run jar2024
./entrar
gazebo
```
Si abre el simulador Gazebo, quiere decir que todo funciona correctamente.

## Contribuciones y Feedback

Si deseas contribuir a este repositorio o tienes sugerencias para mejorar los materiales del taller, no dudes en abrir un issue o realizar un pull request. Tu feedback es invaluable para mejorar futuras ediciones del taller.

## Contacto

Si tienes preguntas específicas sobre el taller o necesitas más información, puedes entrar al canal de [Discord](https://discord.gg/ppyX5qg6aX).

¡Gracias por participar en el Taller de ROS2 en la JAR2024!



