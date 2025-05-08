# `koc_oj4_zed` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

## Description

This package have written to Zed stereo camera. It verifies that the positional tracking is healthy. Also it's check that depth in an given confidency say that there isn't any object in 50cm distance.

## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/Kocsi-HorvathMartin/koc_oj4_zed

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select koc_oj4_zed --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch ros2_py_template launch_example1.launch.py
```

## Graph

``` mermaid

graph TD
    subgraph koc_oj4_zed
        ZED_ODOM[zed_odom.py]
        ZED_DEPTH_FILTER[zed_depth_filter.py]
    end

    ODOM[~/odom] --> ZED_ODOM
    STATUS[~/odom/status] --> ZED_ODOM

    DEPTH[~/depth/depth_registered] --> ZED_DEPTH_FILTER
    CONFIDENCE[~/confidence/confidence_map] --> ZED_DEPTH_FILTER

```