import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'chatter', self.string_callback, 10)
        self.numeric_subscription = self.create_subscription(Int8, 'numeric_chatter', self.numeric_callback, 10)

        self.subscription  # prevent unused variable warning
        self.numeric_subscription  # prevent unused variable warning

    def string_callback(self, msg):
        self.get_logger().info(f'I heard a string message: {msg.data!r}')

    def numeric_callback(self, msg):
        self.get_logger().info(f'I heard a numeric message: {msg.data!r}')


def main(args=None):
    rclpy.init(args=args)
    listener = Listener()
    rclpy.spin(listener)


if __name__ == '__main__':
    main()

