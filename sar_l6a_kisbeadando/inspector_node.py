import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class InspectorSubscriber(Node):
    def __init__(self):
        super().__init__('inspector_node')
        self.subscription = self.create_subscription(
            String,
            'conveyor_belt',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        data = msg.data
        if 'NOK' in data:
            self.get_logger().warn(f' Hibás alkatrész: {data}')
        else:
            self.get_logger().info(f' Alkatrész elfogadva: {data}')

def main(args=None):
    rclpy.init(args=args)
    node = InspectorSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
