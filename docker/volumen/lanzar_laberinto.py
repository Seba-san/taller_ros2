from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, TimerAction,IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import ExecuteProcess
import numpy as np
import random
from launch.launch_description_sources import PythonLaunchDescriptionSource


def rpy_to_rotation_matrix(roll, pitch, yaw):
    # Convertir ángulos de grados a radianes si es necesario
    #roll = np.radians(roll)
    #pitch = np.radians(pitch)
    #yaw = np.radians(yaw)

    # Matriz de rotación alrededor del eje X
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(roll), -np.sin(roll)],
                    [0, np.sin(roll), np.cos(roll)]])

    # Matriz de rotación alrededor del eje Y
    R_y = np.array([[np.cos(pitch), 0, np.sin(pitch)],
                    [0, 1, 0],
                    [-np.sin(pitch), 0, np.cos(pitch)]])

    # Matriz de rotación alrededor del eje Z
    R_z = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                    [np.sin(yaw), np.cos(yaw), 0],
                    [0, 0, 1]])

    # Matriz de rotación combinada
    R = np.dot(R_z, np.dot(R_y, R_x))

    return R


def generate_launch_description():

    # Obtener los valores de configuración
    
    posibles_valores_yaw=[0.0,np.pi/2,np.pi,-np.pi/2]
    yaw=random.choice(posibles_valores_yaw)
    posibles_valores_roll=[0.0,np.pi]
    roll=random.choice(posibles_valores_roll)
    x = -0.75
    y = -5.5
    z = 0.0
    #yaw = np.pi
    roll=0.0
    R=rpy_to_rotation_matrix(roll,0.0,yaw)
    print('Orientacion: ',yaw)
    
    offset=np.array([[x,y,z,]]).T
    T=np.dot(R,offset)
    #import pdb;pdb.set_trace()
    x=T[0][0]
    y=T[1][0]
    z=T[2][0]

    LD=LaunchDescription()
    start_gazebo=ExecuteProcess(cmd=['ros2', 'launch', 'gazebo_ros', 'gazebo.launch.py', 'gui:=0','verbose:=1'])
    # Comando para lanzar Gazebo con el modelo especificado en la posición deseada
    spawn_entity = ExecuteProcess(
        cmd=[
            'ros2', 'run', 'gazebo_ros', 'spawn_entity.py',
            '-entity', 'laberinto',
            '-x', str(x), '-y', str(y), '-z', str(z), '-Y', str(yaw),'-R', str(roll),
            '-file', '/root/catkin_ws/volumen/models/laberinto/model.sdf'  # Asegúrate de cambiar esto por la ruta correcta a tu archivo model.sdf
        ],
        output='screen'
    )
    
    spawn_turtlebot3 = ExecuteProcess(cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'spawn_turtlebot3.launch.py'],output='screen')
    
    # Lanzar Gazebo sin un mundo especificado, se asume que el mundo ya contiene las configuraciones necesarias

    spawn_delay=TimerAction(actions=[spawn_entity],period=2.0)
    spawn_delay_turtle=TimerAction(actions=[spawn_turtlebot3],period=2.0)

    LD.add_entity(start_gazebo)
    LD.add_entity(spawn_delay)
    LD.add_entity(spawn_delay_turtle)
    
    
    return LD
    