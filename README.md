# isaac_launch
Scrach pad for testing isaac-ros repositories
  - sudo apt install -y python3-natsort
  - ros2 launch isaac_launch isaac_launch.py

**This is working but not well**
PeopleNet Model --> https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/peoplenet
```
cd /workspaces/isaac_ros-dev/src/isaac_launch/utils && \
  ./scripts/setup_model.sh --height 1080 --width 1920 --precision int8 \
  --config-file /workspaces/isaac_ros-dev/src/isaac_launch/utils/resources/peoplenet_config.pbtxt \
  --model-link https://api.ngc.nvidia.com/v2/models/nvidia/tao/peoplenet/versions/deployable_quantized_v2.5/zip \
  --model-file-name resnet34_peoplenet_int8.etlt
```

**This is working but not well**
DashcamNet Model --> https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/dashcamnet/files
```
cd /workspaces/isaac_ros-dev/src/isaac_launch/utils && \
  ./scripts/setup_model.sh --height 1080 --width 1920 --precision fp32 \
  --config-file /workspaces/isaac_ros-dev/src/isaac_launch/utils/resources/dashcamnet_config.pbtxt \
  --model-link https://api.ngc.nvidia.com/v2/models/nvidia/tao/dashcamnet/versions/pruned_v1.0.2/zip \
  --model-file-name resnet18_dashcamnet_pruned.etlt
```

**This is working but not well**
TrafficCamNet Model --> https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/trafficcamnet
```
cd /workspaces/isaac_ros-dev/src/isaac_launch/utils && \
  ./scripts/setup_model.sh --height 1080 --width 1920 --precision fp32 \
  --config-file /workspaces/isaac_ros-dev/src/isaac_launch/utils/resources/trafficcamnet_config.pbtxt \
  --model-link https://api.ngc.nvidia.com/v2/models/nvidia/tao/trafficcamnet/versions/pruned_v1.0.2/zip \
  --model-file-name resnet18_trafficcamnet_pruned.etlt
```


FaceDetect-IR Model --> https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/facedetectir