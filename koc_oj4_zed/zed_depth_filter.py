import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge


class DepthMinFilter(Node):
    def __init__(self):
        super().__init__('depth_min_filter')

        self.bridge = CvBridge()
        self.depth_image = None
        self.conf_image = None

        self.depth_sub = self.create_subscription(
            Image,
            '/zed/depth/depth_registered',
            self.depth_callback,
            10
        )

        self.conf_sub = self.create_subscription(
            Image,
            '/zed/confidence/confidence_map',
            self.conf_callback,
            10
        )

        self.get_logger().info("DepthMinFilter node started.")

    def depth_callback(self, msg):
        try:
            self.depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            self.try_process()
        except Exception as e:
            self.get_logger().error(f"Error in depth callback: {e}")

    def conf_callback(self, msg):
        try:
            self.conf_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            self.try_process()
        except Exception as e:
            self.get_logger().error(f"Error in confidence callback: {e}")

    def try_process(self):
        if self.depth_image is None or self.conf_image is None:
            return

        confidence_mask = self.conf_image >= 50  # Confidence threshold

        valid_depths = np.where(confidence_mask, self.depth_image, np.nan)
        min_depth = np.nanmin(valid_depths)

        # Threshold for the minimum depth
        depth_threshold = 0.5

        if np.isnan(min_depth):
            self.get_logger().warn("No valid depth values found.")
        elif min_depth < depth_threshold:
            self.get_logger().error(f"Minimum depth {min_depth:.2f} meters is below the threshold of {depth_threshold:.2f} meters!")

        self.depth_image = None
        self.conf_image = None

def main(args=None):
    rclpy.init(args=args)
    node = DepthMinFilter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()