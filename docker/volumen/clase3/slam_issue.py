import rclpy
from rclpy.node import Node
#import tf_transformations
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
from rosgraph_msgs.msg import Clock
from rclpy.qos import QoSProfile, ReliabilityPolicy



class OdomToBaseScanPublisher(Node):
    def __init__(self):
        super().__init__('odom_to_base_scan_tf2_broadcaster')
        self.broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.publish_tf)
        qos_profile = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

        # Subscriber to the /clock topic con el QoS ajustado
        self.clock_subscriber = self.create_subscription( Clock,'/clock',self.clock_callback,qos_profile )
        self.sim_time=None
        
    def clock_callback(self, clock_msg):
        # Update simulation time whenever a new clock message is received
        self.sim_time = clock_msg.clock


    def publish_tf(self):
        if self.sim_time is None:
            return
        
    	   

        t = TransformStamped()
        # Llena los campos necesarios para el mensaje TransformStamped
        t.header.stamp = self.sim_time
        t.header.frame_id = 'base_footprint'
        t.child_frame_id = 'base_scan'

        # Configura la transformación
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        t.transform.rotation.x=0.0
        t.transform.rotation.y=0.0
        t.transform.rotation.z=0.0
        t.transform.rotation.w=1.0
        
        #t.transform.rotation = tf_transformations.quaternion_from_euler(0, 0, 0)

        # Envía la transformación
        self.broadcaster.sendTransform(t)
        t.child_frame_id = 'base_link'
        self.broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = OdomToBaseScanPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

