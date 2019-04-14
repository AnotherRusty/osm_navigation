# osm_navigation

### 更新：
launch文件取消了osm_helper节点, 增加fake_localization节点，发布odom->map的tf关系


### 使用方法：
STEP 1: 运行 rbx1 模拟机器人
```bash
$ roslaunch rbx1_bringup fake_turtlebot.launch
```

STEP 2: 运行导航
```bash
$ roslaunch osm_nav nav.launch
```

---
## TIPS
把source添加到.bashrc 就不需要每次都手动打了。
```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

