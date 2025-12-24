import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StdinPublisher(Node):
    def __init__(self):
        super().__init__('stdin_publisher')
        self.publisher_ = self.create_publisher(String, '/stdin', 10)
        self.get_logger().info('Type something and press Enter...')

    def run(self):
        while rclpy.ok():
            try:
                line = input()
            except EOFError:
                break
            msg = String()
            msg.data = line
            self.publisher_.publish(msg)

def main():
    rclpy.init()
    node = StdinPublisher()
    node.run()
    node.destroy_node()
    rclpy.shutdown()
