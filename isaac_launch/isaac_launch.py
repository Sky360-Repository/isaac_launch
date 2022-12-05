import os

from ament_index_python.packages import get_package_share_directory
from launch import actions, LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    
    isaac_ros_detectnet_package_dir = get_package_share_directory('isaac_ros_detectnet')
    
    video_file = os.path.join(get_package_share_directory('isaac_launch'), 'videos', 'plane_flying_past2.mkv')
    #video_file = os.path.join(get_package_share_directory('isaac_launch'), 'videos', 'brad_drone_1.mp4')
    camera_info_file = os.path.join(get_package_share_directory('isaac_launch'), 'config', 'camera_info.yaml')
    config = os.path.join(get_package_share_directory('isaac_launch'), 'config', 'params_launch.yaml')

    return LaunchDescription([
        #actions.ExecuteProcess(
        #    cmd=['ros2', 'bag', 'play', '-l',
        #         os.path.join(my_package_dir, 'detectnet_rosbag')]
        #),

        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource([os.path.join(
        #        isaac_ros_detectnet_package_dir, 'launch'),
        #        '/isaac_ros_detectnet.launch.py'])
        #),

        Node(
            name='usb_cam',
            package='usb_cam',
            executable='usb_cam_node_exe',
            remappings=[('image_raw', 'camera_image')]
        ),

        Node(
            name='camera_simulator',
            package='camera_simulator',
            executable='camera_simulator',
            parameters = [config],
            remappings=[('image/image_raw', 'video_image')],
            arguments=[
                '--type', 'video', 
                '--path', video_file, 
                '--calibration_file', camera_info_file,
                '--loop']
        ),

        Node(
            package='isaac_ros_detectnet',
            executable='isaac_ros_detectnet_visualizer.py',
            name='detectnet_visualizer'
        ),

        Node(
            package='rqt_image_view',
            executable='rqt_image_view',
            name='image_view',
            #arguments=['/detectnet_processed_image']
            arguments=['video_image']
        )
    ])
