#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from math import pi
import random

MAX_RANGE = 20.0
OBSTACLE_INTERVAL = 3.0   # new obstacles per ? sec


def random_obstacle():
    obstacle_angle = random.randint(0, 360)
    obstacle_distance = random.uniform(0.3, 2.5)
    return (obstacle_angle, obstacle_distance)


def get_scan(obstacles):
    ranges = [float('inf') for i in range(360)]
    for obstacle in obstacles:
        mid = obstacle[0]   # obstacle mid angle
        left = mid - 3    # width +/-5 degrees
        right = mid + 3
        dist = obstacle[1]
        for angle in range(left, right):
            index = (angle+360)%360
            ranges[index] = dist
    return ranges


rospy.init_node('fake_laser_scan', anonymous=False)
scan_pub = rospy.Publisher('scan', LaserScan, queue_size=10)


scan = LaserScan()
scan.header.stamp = rospy.Time.now()
scan.header.frame_id = 'laser'
scan.angle_min = 0.0
scan.angle_max = 2 * pi
scan.angle_increment = pi / 180.0
scan.range_min = 0.15
scan.range_max = MAX_RANGE

rate = rospy.Rate(30)
next_time = rospy.Time.now()

while not rospy.is_shutdown():
    obstacles = [random_obstacle() for i in range(3)]   # random 3 obstacles
    if rospy.Time.now() > next_time:
        scan.ranges = get_scan(obstacles)
        next_time += rospy.Duration(3.0)

    scan_pub.publish(scan)
    rate.sleep()
    