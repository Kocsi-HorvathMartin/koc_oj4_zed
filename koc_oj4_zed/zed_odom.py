import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from zed_interfaces.msg import TrackingStatus

class ZedOdomListener(Node):
    def __init__(self):
        super().__init__('zed_odom_listener')

        self.create_subscription(
            Odometry,
            '/zed/odom',
            self.odom_callback,
            10
        )

        self.get_logger().info('ZED Odometry Listener Node has been started.')

    def odom_callback(self, msg: Odometry):
        position = msg.pose.pose.position
        self.get_logger().info(
            f"Position - x: {position.x:.2f}, y: {position.y:.2f}, z: {position.z:.2f}"
        )