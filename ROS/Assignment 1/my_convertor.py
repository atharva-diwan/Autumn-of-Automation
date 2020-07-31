#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
from my_pkg.msg import Topic1

import numpy as np
result = Float64MultiArray()

def quaternion_to_euler(w, x, y, z):
	

	sinr_cosp = 2 * (w * x + y * z)
	cosr_cosp = 1 - 2 * (x**2 + y**2)
	roll = np.arctan2(sinr_cosp, cosr_cosp)

	sinp = 2 * (w * y - z * x)
	pitch = np.where(np.abs(sinp) >= 1,
		             np.sign(sinp) * np.pi / 2,
		             np.arcsin(sinp))

	siny_cosp = 2 * (w * z + x * y)
	cosy_cosp = 1 - 2 * (y**2 + z**2)
	yaw = np.arctan2(siny_cosp, cosy_cosp)

	return roll, pitch, yaw

def callback(msg):
	result.data=quaternion_to_euler(msg.x,msg.y,msg.z,msg.w)
	rospy.loginfo(result)
def main():
    	

	rospy.init_node('my_convertor', anonymous=True)
	sub=rospy.Subscriber("Topic1", Topic1, callback)
   	r=rospy.Rate(1)
	pub=rospy.Publisher("Topic2", Float64MultiArray,queue_size=1)
	
	while not rospy.is_shutdown():
		pub.publish(result)
		r.sleep()
   
if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptionException:
		pass

       
