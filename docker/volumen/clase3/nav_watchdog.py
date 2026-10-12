#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import Twist
from action_msgs.msg import GoalStatusArray
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy


class VelocityWatchdog(Node):
    def __init__(self):
        super().__init__('velocity_watchdog')

        # Publicador al tópico puente hacia Gazebo
        self.pub_twist = self.create_publisher(Twist, '/nav_cmd_vel', 10)

        # QoS compatible con el Action Server de ROS 2 (Transient Local + Reliable)
        action_status_qos = QoSProfile(
            depth=10,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE
        )

        self.status_sub = self.create_subscription(
            GoalStatusArray,
            '/navigate_to_pose/_action/status',
            self.status_callback,
            action_status_qos
        )

        self.is_navigating = False
        # Timer periódico a 20 Hz (versión robusta): cuando no hay navegación activa,
        # publica ceros continuamente para anular cualquier residuo de velocidad en Gazebo.
        self.timer = self.create_timer(0.05, self.timer_callback)
        self.get_logger().info('>>> VelocityWatchdog ROBUSTO (Timer continuo 20 Hz en reposo) iniciado. <<<')

    def status_callback(self, msg: GoalStatusArray):
        # 1: STATUS_ACCEPTED, 2: STATUS_EXECUTING
        self.is_navigating = any(status.status in [1, 2] for status in msg.status_list)

    def timer_callback(self):
        if not self.is_navigating:
            self.pub_twist.publish(Twist())


def main():
    rclpy.init()
    node = VelocityWatchdog()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
