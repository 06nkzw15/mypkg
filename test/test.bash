#!/bin/bash
set -e

# workspace directory
WS=${1:-$HOME}/ros2_ws

cd "$WS"

# ROS 環境を source
source /opt/ros/jazzy/setup.bash
source install/setup.bash

# build
colcon build

# 実行テスト（10秒）
timeout 10 ros2 launch mypkg stdin_publisher.launch.py > /tmp/mypkg.log 2>&1 || true

# ログ表示
cat /tmp/mypkg.log

# 期待されるログをチェック
grep -q "Type something and press Enter" /tmp/mypkg.log

