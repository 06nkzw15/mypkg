# SPDX-FileCopyrightText: 2025 Taiki Nakazawa
# SPDX-License-Identifier: BSD-3-Clauseimport rclpy

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

class StdinPublisher(Node):
    def __init__(self):
        super().__init__('stdin_publisher')
        self.pub = self.create_publisher(String, '/stdin', 10)
        self.get_logger().info('Type something and press Enter...')

        threading.Thread(target=self._read_loop, daemon=True).start()

    def _read_loop(self):
        while rclpy.ok():
            try:
                line = input()
            except EOFError:
                break
            msg = String()
            msg.data = line
            self.pub.publish(msg)
            self.get_logger().info(f'Published: {line}')

def main():
    rclpy.init()
    node = StdinPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


