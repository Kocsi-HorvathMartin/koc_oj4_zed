from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([ 
        # Launch the ZED Depth Filter Node
        Node(
            package='koc_oj4_zed',  # Your package name
            executable='zed_depth_filter',  # Name of the Python executable for this node
            name='zed_depth_filter',
            output='screen',
            parameters=[{'filter_strength': 0.5}],
            remappings=[('/zed/zed_node/depth/depth_registered', '/my_robot/depth_image')]
        ),
        
        # Launch the ZED Odometry Node
        Node(
            package='koc_oj4_zed',  # Your package name
            executable='zed_odom',  # Name of the Python executable for this node
            name='zed_odom',
            output='screen',
            parameters=[{'odom_topic': '/zed/zed_node/odom'}],
            remappings=[('/my_robot/pose', '/robot/pose')]
        ),
    ])
