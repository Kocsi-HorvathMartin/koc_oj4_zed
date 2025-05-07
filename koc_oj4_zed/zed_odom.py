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

        self.create_subscription(
            TrackingStatus,
            '/zed/odom/status',
            self.status_callback,
            10
        )

        self.get_logger().info('ZED Odometry Listener Node has been started.')

    def odom_callback(self, msg: Odometry):
        position = msg.pose.pose.position
        self.get_logger().info(
            f"Position - x: {position.x:.2f}, y: {position.y:.2f}, z: {position.z:.2f}"
        )

    def status_callback(self, msg: TrackingStatus):
        status_dict = {
            0: "OFF",
            1: "OK",
            2: "SEARCHING",
            3: "FPS_TOO_LOW"
        }

        status_text = status_dict.get(msg.status, "UNKNOWN")
        if msg.status != 1:
            self.get_logger().error(f"Tracking Error! Status: {status_text}")

def main(args=None):
    rclpy.init(args=args)
    node = ZedOdomListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()