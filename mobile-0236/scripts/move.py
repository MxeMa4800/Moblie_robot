#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def publish_cmd_vel():
    # Initialize the ROS node
    rospy.init_node('cmd_vel_publisher', anonymous=True)

    # Create a publisher for the cmd_vel topic
    cmd_vel_pub = rospy.Publisher('/velocity_controller/cmd_vel', Twist, queue_size=10)

    # Create a Twist message
    cmd_msg = Twist()
    cmd_msg.linear.x = 0.2
    cmd_msg.linear.y = 0.0
    cmd_msg.linear.z = 0.0
    cmd_msg.angular.x = 0.0
    cmd_msg.angular.y = 0.0
    cmd_msg.angular.z = 1.0

    # Publish the message repeatedly
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        cmd_vel_pub.publish(cmd_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_cmd_vel()
    except rospy.ROSInterruptException:
        pass