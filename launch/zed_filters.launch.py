from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='koc_oj4_zed',
            executable='zed_odom.py',
            name='zed_odom_listener',
            output='screen'
        ),
        Node(
            package='koc_oj4_zed',
            executable='zed_depth_filter.py',
            name='depth_min_filter',
            output='screen'
        )
    ])