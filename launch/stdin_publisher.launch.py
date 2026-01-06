# SPDX-FileCopyrightText: 2025 Taiki Nakazawa
# SPDX-License-Identifier: BSD-3-Clause
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

