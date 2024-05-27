#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSDurabilityPolicy, QoSReliabilityPolicy
from std_msgs.msg import String
from rclpy.duration import Duration

def create_qos_policy():
    # Configura el objeto QoS
    custom_qos = QoSProfile(
        history=QoSHistoryPolicy.KEEP_ALL,
        reliability=QoSReliabilityPolicy.RELIABLE,
        durability=QoSDurabilityPolicy.TRANSIENT_LOCAL
    )
    return custom_qos

class PublisherQoS(Node):
    def __init__(self):
        super().__init__('qos_test')
        # Configuramos el publisher con diferentes QoS
        self.publisher = self.create_publisher(String, 'topic_qos', create_qos_policy())
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        message = String()
        message.data = f'Mensaje número: {self.count}'
        self.get_logger().info(f'Se publicó: "{message.data}"')
        self.publisher.publish(message)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    publisher_qos = PublisherQoS()
    rclpy.spin(publisher_qos)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
