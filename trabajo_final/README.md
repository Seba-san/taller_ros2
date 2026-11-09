# Trabajo Final de Cierre — Taller de ROS 2 (Modalidad Híbrida JAR2026)

Este documento detalla los requisitos, plazos, rúbrica de evaluación y criterios de certificación para el **Trabajo Final Acotado** que concluye la edición 2026 del Taller de ROS 2.

---

## Criterios de Certificación

| Certificado | Requisitos de Obtención |
| :--- | :--- |
| **Certificado de Asistencia** | Requiere el **70%** de participación, que en esta modalidad híbrida equivale explícitamente a: **1)** Asistir al menos a una (1) clase presencial, **2)** Completar el formulario de propuesta en Google Forms, y **3)** Solicitar y participar de la clase de consulta individual (máximo 1 hs). |
| **Certificado de Aprobación** | Requiere completar y tener el **100%** del Trabajo Final aprobado, cumpliendo satisfactoriamente los requisitos técnicos y la rúbrica de evaluación. |

> [!IMPORTANT]
> **Carácter Individual y Autoría**:
> El trabajo es estrictamente **individual** y de **producción estricta** del estudiante. Cualquier desarrollo o modificación incorporada debe ser clara, **evidente**, explicable y el estudiante debe estar en condiciones de poder **defender** cada decisión técnica tomada tanto en la consulta como en el video.

---

## Requisitos Técnicos Obligatorios

El trabajo final consiste en el desarrollo e integración de un sistema funcional en ROS 2 que cumpla obligatoriamente con los siguientes 6 requisitos:

1. **Package de ROS 2**: Creación y configuración de un `package` propio con sus dependencias y estructura adecuada.
2. **Nodo de ROS 2**: Implementación de al menos un `nodo` propio desarrollado en Python o C++.
3. **Comunicación y QoS**: Implementar por lo menos **2 publicadores** y **2 suscriptores** configurados con distinta Calidad de Servicio (**QoS**).
4. **Launchfile**: Configuración de un `launchfile` que automatice el despliegue y lanzamiento sincronizado de los nodos y componentes.
5. **Modificación del URDF y TF**: Modificar el modelo **URDF** del robot **Burger** añadiendo un elemento o accesorio personalizado (antena, colores, textura, accesorio adicional, etc.) que resulte claramente visible tanto en la simulación (Gazebo) como en **RViz**, garantizando su correcta vinculación y referencia en el árbol de transformaciones **TF** (`tf2`).
6. **Prueba en Simulación**: Ejecutar y validar el funcionamiento del sistema en simulación (se puede reutilizar el entorno del laberinto u otro escenario provisto).

---

## Etapas de Ejecución y Cronograma

1. **Envío de Propuesta**:
   - Completar y enviar previamente el formulario de planificación en Google Forms: [https://forms.gle/23726Nmo9ajpUsoi9](https://forms.gle/23726Nmo9ajpUsoi9), detallando cómo se abordará cada requisito técnico.
2. **Período de Desarrollo y Consulta Individual**:
   - Una vez aprobada la propuesta, se dispondrá de **1 semana** para la ejecución técnica y preparación del material.
   - Cada estudiante contará con **1 clase de consulta individual** virtual de un máximo de **1 hs** de duración para evacuar dudas técnicas y revisar el avance.
3. **Entrega y Video de Presentación**:
   - Entrega del repositorio personal con el código fuente desarrollado.
   - Grabación y entrega de un **video** de presentación y defensa técnica con una duración máxima de **10 minutos** y un soporte visual de no más de **5** slides (diapositivas).
   - En el video se debe demostrar y ejemplificar el funcionamiento del sistema visualizando las transformaciones y tópicos en **RViz** y la topología en **rqt_graph**.
   - La captura o reproducción de datos mediante **Rosbag** es un plus que será muy bien valorado en la evaluación.

---

## Rúbrica  de Evaluación

La evaluación aplica tres niveles de desempeño graduados según los verbos de acción alcanzados:

| Criterio a Evaluar | Falta trabajar (Inicial) | Suficiente (Aplicación / Aprobado) | Maestría (Diseño / Sobresaliente) |
| :--- | :--- | :--- | :--- |
| **1. Paquete y Nodo propio** (`package` y `nodo` en ROS 2) | **Identifica** con dificultad la estructura interna; el **package** no compila o el **nodo** no ejecuta. | **Implementa** su propio **package** y **nodo** funcional; compila y corre sin errores en ROS 2. | **Diseña** un **package** modular y desacoplado, aplicando buenas prácticas y código limpio de **nodo** en ROS 2. |
| **2. Comunicación y QoS** (mínimo 2 pub / 2 sub con distinta QoS) | **Configura** de forma incompleta; menos de **2 publicadores** o **2 suscriptores**, o no define la política de **QoS**. | **Aplica** la comunicación con al menos **2 publicadores** y **2 suscriptores** con distinta **QoS** operativa. | **Optimiza** el flujo telemétrico, adaptando y justificando cada perfil de **QoS** entre los **2 publicadores** y **2 suscriptores**. |
| **3. Robot Burger y TF** (URDF evidente en RViz y simulación) | **Describe** o modifica con fallas el robot **Burger**; no se distingue el cambio en el **URDF** o falta en el árbol **TF** (tf2). | **Modifica** el **URDF** del robot **Burger** con un elemento **evidente** visible en **RViz** y **simulación**, enlazado a **TF** (tf2). | **Integra** una modificación visual clara y articulada cinemáticamente en el modelo **URDF** del **Burger** y su árbol **TF** (tf2). |
| **4. Launchfile y Simulación** (arranque del mundo y laberinto) | **Ejecuta** comandos sueltos a mano o el **launchfile** falla al abrir el entorno de **simulación**. | **Automatiza** el arranque del sistema y la **simulación** (reutilizando el **laberinto**) mediante un único **launchfile**. | **Orquesta** un **launchfile** robusto y parametrizado que levanta nodos y **simulación** en el **laberinto** sin bloqueos. |
| **5. Video de Demostración** ($\le$ 5 slides, $\le$ 10 min, RViz y rqt_graph) | **Expone** en el **video** excediendo los límites (más de **10 minutos** o **5 slides**), o sin mostrar **RViz** ni **rqt_graph**. | **Demuestra** el sistema en un **video** de hasta **10 minutos** y **5 slides**, mostrando **RViz** y **rqt_graph** en vivo. | **Sustenta** con claridad y síntesis técnica el funcionamiento a tiempo en el **video** ($\le$ **5 slides** y **10 minutos**), explicando **RViz** y **rqt_graph**. |
| **6. Autoría y Defensa Técnica** (producción estricta e individual) | **Reproduce** código externo sin autoría original; no puede explicar su solución ni **defender** su desarrollo técnico. | **Defiende** con claridad su trabajo **individual** de **producción estricta** y modificación **evidente**. | **Justifica** con solvencia teórica y técnica cada decisión tomada, logrando **defender** con dominio total su **producción estricta** individual. |
| **Plus: Registro con Rosbag** (herramienta opcional destacada) | **Reconoce** la herramienta pero no logra registrar ni reproducir tópicos con **rosbag**. | **Utiliza** **rosbag** para grabar y reproducir fidedignamente los datos del sistema. | **Analiza** y valida datos grabados con **rosbag** aplicando filtros y reproducción determinista. |

---

## Documentación en PDF para Descarga

Toda la información anterior (instrucciones, requisitos y rúbrica completa) se encuentra compilada en un único documento PDF para su descarga o impresión:

- [📄 **Descargar Instrucciones del Trabajo Final y Rúbrica Completa (PDF)**](./TRABAJO_FINAL_Y_RUBRICA.pdf)

---

## 🎥 Presentaciones y Videos de los Estudiantes

En esta sección se centralizarán y publicarán los enlaces a los repositorios y videos de presentación del trabajo final entregados por cada participante de la edición 2026:

| Estudiante | Proyecto / Modificación | Repositorio GitHub | Video de Presentación | Estado |
| :--- | :--- | :---: | :---: | :---: |
| *(Próxima entrega)* | — | — | — | *En desarrollo* |

*(Los enlaces a los videos y repositorios se irán incorporando a medida que los estudiantes completen sus entregas y defensas).*
