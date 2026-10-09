import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy

def create_qos_policy():
    custom_qos = QoSProfile(
        reliability=ReliabilityPolicy.RELIABLE,
        durability=DurabilityPolicy.TRANSIENT_LOCAL,
        history=HistoryPolicy.KEEP_ALL
        # depth=10,  # Solo aplica si history=HistoryPolicy.KEEP_LAST
        # deadline=rclpy.duration.Duration(seconds=1)
    )
    return custom_qos

class SubscriberQos(Node):
    def __init__(self):
        super().__init__('qos_test_subs')
        self.subscriber_ = self.create_subscription(
            String,
            'topic_qos',
            self.topic_callback,
            create_qos_policy()
        )
        self.count_ = 0
        # self.subscriber_.add_event_handler

    def topic_callback(self, msg):
        self.get_logger().info(f"Se recibió: '{msg.data}', mensaje número {self.count_}")
        self.count_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberQos()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()