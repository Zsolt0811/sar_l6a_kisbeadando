import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ConveyorPublisher(Node):
    def __init__(self):
        super().__init__('conveyor_node')
        self.publisher_ = self.create_publisher(String, 'conveyor_belt', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.item_id = 0

    def timer_callback(self):
        self.item_id += 1
        status = 'NOK' if random.random() < 0.2 else 'OK'

        msg = String()
        msg.data = f'Item #{self.item_id}:{status}'

        self.publisher_.publish(msg)
        self.get_logger().info(f'Futószalag továbbítva: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = ConveyorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
