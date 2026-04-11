import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveForwardNode(Node):

    def __init__(self):
        super().__init__('move_forward_node')

        # 创建发布者，发布到 /cmd_vel
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # 定时器，每0.5秒执行一次
        self.timer = self.create_timer(0.5, self.move_robot)

    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.2  # 前进速度
        msg.angular.z = 0.0  # 不旋转

        self.publisher_.publish(msg)
        self.get_logger().info("Robot moving forward...")

def main(args=None):
    rclpy.init(args=args)
    node = MoveForwardNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
