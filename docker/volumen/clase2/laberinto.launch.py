
from launch import LaunchDescription as Launch
from launch.actions import IncludeLaunchDescription as Include
from launch.launch_description_sources import PythonLaunchDescriptionSource as Source
from launch.substitutions import PathJoinSubstitution as Path
from launch_ros.substitutions import FindPackageShare as Find
from launch.actions import TimerAction
from launch.actions import ExecuteProcess

def generate_launch_description():
    x=0.0
    y=0.0
    z=0.0
    model_path='/root/catkin_ws/volumen/models/laberinto/model.sdf'
    ld=Launch()
    start_gazebo = Include( Source( Path([Find('gazebo_ros'), 'launch', 'gazebo.launch.py'])), 
                           launch_arguments={'gui': '1', 'verbose': '1'}.items())
    
    spawn_turtlebot3 = Include( Source( Path([Find('turtlebot3_gazebo'), 'launch', 'spawn_turtlebot3.launch.py'])),
                               launch_arguments={'output': 'screen','x_pose':'1.0','y_pose':'1.0'}.items())
    
    spawn_laberinto = ExecuteProcess(cmd=[
            'ros2', 'run', 'gazebo_ros', 'spawn_entity.py',
            '-entity', 'laberinto',
            '-x', str(x), '-y', str(y), '-z', str(z),
            '-file', model_path],
        output='screen'
    )

    segundo=TimerAction(period=5.0,actions=[spawn_laberinto])
    tercer=TimerAction(period=10.0,actions=[spawn_turtlebot3])
    ld.add_action(start_gazebo)
    ld.add_action(segundo)
    ld.add_action(tercer)
 
    return  ld
