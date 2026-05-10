# AI Robotics Sim - Quick Start

## 1. 启动 Docker Desktop

Windows 打开 Docker Desktop。

---

## 2. 进入 WSL

```bash
wsl
```

---

## 3. 进入项目目录

```bash
cd ~/ai-robotics-sim
```

---

## 4. 启动 ROS2 容器

```bash
docker start ros2_dev_gui
```

---

## 5. 进入容器

```bash
docker exec -it ros2_dev_gui bash
```

---

## 6. 进入 ROS2 Workspace

```bash
cd /home/ros/ai-robotics-sim/ros2_ws
```

---

## 7. 加载 ROS2

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
```

---

## 8. 设置 TurtleBot3

```bash
export TURTLEBOT3_MODEL=burger
```

---

## 9. 启动完整系统

```bash
ros2 launch patrol_robot patrol.launch.py
```