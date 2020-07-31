#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

PI = 3.1415926535897
x = 0
y = 0
z = 0
yaw = 0

def poseCallback(pose_message):

    global x, y, z, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(speed, distance, is_forward):
    velocity_message = Twist()

    x0 = x
    y0 = y
    if is_forward:
    	velocity_message.linear.x = speed
    else:
	velocity_message.linear.x = -abs(speed)
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)

    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    while True:

        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()

        distance_moved = distance_moved + abs(0.5 * math.sqrt((x - x0)**2 + (y - y0)**2))


        if distance_moved > distance:

            break

    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)

def rotate(speed,angle,clockwise):
        angular_speed = speed*2*PI/360
        relative_angle = angle*2*PI/360
	global yaw
	vel_msg = Twist() 
    	vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
	theta0=yaw
	if clockwise:
        	vel_msg.angular.z = -abs(angular_speed)
        else:
        	vel_msg.angular.z = abs(angular_speed)
	loop_rate=rospy.Rate(10)
	cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Setting the current time for distance calculation
        t0 = rospy.Time.now().to_sec()
        current_angle = 0.0

        while True:

		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angular_speed*(t1-t0)
		loop_rate.sleep()
		if (current_angle>relative_angle):

			break


        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
	

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        position_topic = '/turtle1/pose'
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)

        time.sleep(2)
	rotate(20,60,0)
        move(1.0, 15.0,1)
	rotate(30,120,1)
	move(1.0,15.0,1)
	move(1.0,3.0,0)
	rotate(20,120,1)
	move(1.0,5.0,1)
        time.sleep(2)

        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('node terminated')
