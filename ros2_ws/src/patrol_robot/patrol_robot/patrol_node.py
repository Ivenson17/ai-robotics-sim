import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class PatrolNode(Node):

    def __init__(self):
        super().__init__('patrol_node')
        self.get_logger().info("Patrol Node Started")

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.timer = self.create_timer(0.1, self.control_loop)

        self.state = "MOVING"

    def scan_callback(self, msg):
        min_dist = min(msg.ranges)

        if min_dist < 0.5:
            self.state = "TURNING"

    def control_loop(self):
        self.get_logger().info(f"Current state: {self.state}")
        
        msg = Twist()

        if self.state == "MOVING":
            msg.linear.x = 0.2

        elif self.state == "TURNING":
            msg.angular.z = 0.5

        self.cmd_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PatrolNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()