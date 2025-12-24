from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='stdin_publisher',
            name='stdin_publisher',
            output='screen',
            emulate_tty=True
        )
    ])

