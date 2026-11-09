# Taller de ROS2 - JAR2026

Este repositorio contiene todos los materiales y recursos utilizados durante el Taller de ROS2 que se llevó a cabo del 3 al 6 de noviembre de 2026, en el marco de la Jornadas Argentinas de Robótica (JAR2026). El taller estuvo diseñado para introducir a los participantes en los fundamentos y herramientas avanzadas de ROS2, cubriendo temas como topics, servicios, TF2, la integración con sistemas de simulación, entre otros.

## Contenidos del Repositorio

En este repositorio encontrarás los siguientes recursos:

- **Trabajo Final**: Carpeta [`trabajo_final/`](./trabajo_final/) con las instrucciones completas, rúbrica de evaluación oficial, documento PDF descargable y espacio para las presentaciones de los estudiantes.
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
./entrar
gz sim
```
Si abre el simulador Gazebo, quiere decir que todo funciona correctamente.

## 📢 Modalidad Híbrida y Trabajo Final (JAR2026)

Debido a la reducción horaria y a la reestructuración de las actividades presenciales durante las jornadas, el taller migra hacia una **modalidad híbrida (cursada mixta)**: tras haber realizado el setup inicial y las primeras clases presenciales en el laboratorio, el cierre y acreditación del curso se realiza mediante la presentación de un **Trabajo Final Acotado** individual con seguimiento y tutoría personalizada.

Toda la información detallada, los requisitos técnicos, las etapas de desarrollo y la rúbrica oficial de evaluación se encuentran en la carpeta dedicada al trabajo final:

👉 [**Acceder a las Instrucciones Completas y Rúbrica del Trabajo Final**](./trabajo_final/README.md)

### Resumen de Certificación:
- **Certificado de Asistencia (70%):** Requiere haber asistido al menos a una (1) clase presencial, completar el formulario de propuesta y solicitar la clase de consulta individual (máximo 1 hs).
- **Certificado de Aprobación (100%):** Requiere completar, entregar y aprobar el Trabajo Final según la rúbrica técnica.
- **Formulario de Propuesta Inicial:** [https://forms.gle/23726Nmo9ajpUsoi9](https://forms.gle/23726Nmo9ajpUsoi9)
- **Documento Oficial en PDF:** Disponible en la carpeta [`trabajo_final/`](./trabajo_final/) ([Instrucciones completas y Rúbrica en PDF](./trabajo_final/TRABAJO_FINAL_Y_RUBRICA.pdf)).

## Ediciones anteriores
Puedes consultar todo el material, código y recursos de la primera edición del taller (JAR 2024) accediendo directamente a su rama correspondiente:
- [**Material completo de la Edición 1**](https://github.com/Seba-san/taller_ros2/tree/edicion_2024)

### Datos de la Encuesta

Al finalizar el taller anterior, se realizó una encuesta de satisfacción para recoger las impresiones y el feedback de los participantes. Los datos recogidos han sido analizados y están disponibles para consulta:

- [Datos de la Encuesta y Gráficos (Edición 1)](https://github.com/Seba-san/taller_ros2/tree/edicion_2024/encuesta_ed1)

En esta carpeta, encontrarás tanto el archivo CSV con las respuestas de la encuesta como varias imágenes con gráficos que resumen visualmente la información recogida.

### Fotos del Evento

Durante el desarrollo del taller se tomaron varias fotos que capturan momentos clave del evento y la participación activa de los asistentes. Estas fotos están disponibles en la siguiente carpeta:

- [Fotos del Taller (Edición 1)](https://github.com/Seba-san/taller_ros2/tree/edicion_2024/fotos)

## Contribuciones y Feedback

Si deseas contribuir a este repositorio o tienes sugerencias para mejorar los materiales del taller, no dudes en abrir un issue o realizar un pull request. Tu feedback es invaluable para mejorar futuras ediciones del taller.

## Contacto

Si tienes preguntas específicas sobre el taller o necesitas más información, puedes entrar al canal de [Discord](https://discord.gg/ppyX5qg6aX).

¡Gracias por participar en el Taller de ROS2 en la JAR2026!
