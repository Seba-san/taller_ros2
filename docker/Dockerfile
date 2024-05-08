# Usar la imagen oficial de ROS2 Humble
FROM osrf/ros:humble-desktop

# Definir variables de entorno para evitar la interacción durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

## Instalar Clang, lld (enlazador de Clang) y herramientas adicionales
#RUN apt-get update && apt-get install -y \
#    clang-12 \
#    lld-12 \
#    build-essential \
#    cmake \
#    git \
#    wget \
#    curl \
#    && rm -rf /var/lib/apt/lists/*
#
## Configurar Clang como el compilador predeterminado
#ENV CC=/usr/bin/clang-12
#ENV CXX=/usr/bin/clang++-12
#ENV LD=/usr/bin/lld-12

RUN apt-get update && apt-get install -y \
    gedit nano

# Configurar el entorno de ROS2
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Configurar el punto de entrada del contenedor
WORKDIR /root
CMD ["bash"]
