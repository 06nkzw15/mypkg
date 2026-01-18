#!/bin/bash
set -e

WS=${1:-$HOME}/ros2_ws

cd "$WS"


source /opt/ros/humble/setup.bash
source install/setup.bash

colcon build

timeout 10 ros2 launch mypkg stdin_publisher.launch.py > /tmp/mypkg.log 2>&1 || true

cat /tmp/mypkg.log

grep -q "Type something and press Enter" /tmp/mypkg.log
