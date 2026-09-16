# Usar la imagen oficial de ROS2 Jazzy
FROM osrf/ros:jazzy-desktop

# Definir variables de entorno para evitar la interacción durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Herramientas de uso general
RUN apt-get update && apt-get install -y \
    gedit nano wget evince \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de ROS2 Jazzy, TurtleBot3 y nueva integración con Gazebo Harmonic
RUN apt-get update && apt-get install -y \
    ros-jazzy-ros-gz \
    ros-jazzy-turtlebot3* \
    ros-jazzy-urdf-tutorial \
    && rm -rf /var/lib/apt/lists/*

# Herramientas de Python y sistema
RUN apt-get update && apt-get install -y \
    python3-pip tree \
    && rm -rf /var/lib/apt/lists/*
    
# Configurar el entorno de ROS2
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
RUN echo "export ROS_DOMAIN_ID=12" >> ~/.bashrc

RUN echo "export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST" >> ~/.bashrc

# Configurar las rutas de modelos para Gazebo Harmonic (GZ_SIM_RESOURCE_PATH)
# Se incluye también GAZEBO_MODEL_PATH por si algún paquete de terceros mantiene la ruta antigua
RUN echo "export GZ_SIM_RESOURCE_PATH=/opt/ros/jazzy/share/turtlebot3_gazebo/models/:/root/ros2_ws/volumen/models" >> ~/.bashrc
RUN echo "export GAZEBO_MODEL_PATH=/opt/ros/jazzy/share/turtlebot3_gazebo/models/:/root/ros2_ws/volumen/models" >> ~/.bashrc

# Configurar el punto de entrada del contenedor
WORKDIR /root
CMD ["bash"]
