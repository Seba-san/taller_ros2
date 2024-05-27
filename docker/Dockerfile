# Usar la imagen oficial de ROS2 Humble
FROM osrf/ros:humble-desktop

# Definir variables de entorno para evitar la interacción durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    gedit nano wget evince

RUN apt-get update && apt-get install -y \
    ros-humble-gazebo-ros-pkgs ros-humble-turtlebot3* ros-humble-urdf-tutorial

RUN apt-get update && apt-get install -y \
	python3-pip tree
    
# Configurar el entorno de ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
RUN echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc
RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
RUN echo "export ROS_DOMAIN_ID=12" >> ~/.bashrc
RUN echo "export ROS_LOCALHOST_ONLY=1" >> ~/.bashrc

RUN echo "export GAZEBO_MODEL_PATH=/usr/share/gazebo-11/models:/opt/ros/humble/share/turtlebot3_gazebo/models/:/root/catkin_ws/volumen/models" >> ~/.bashrc

# Configurar el punto de entrada del contenedor
WORKDIR /root
CMD ["bash"]
