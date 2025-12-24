from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stdin_publisher',
            executable='stdin_publisher_node',
            name='stdin_publisher',
            output='screen'
        )
    ])
:

