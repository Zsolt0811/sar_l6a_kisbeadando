from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sar_l6a_kisbeadando',
            executable='conveyor_node',
            name='conveyor'
        ),
        Node(
            package='sar_l6a_kisbeadando',
            executable='inspector_node',
            name='inspector',
            output='screen'
        ),
    ])
