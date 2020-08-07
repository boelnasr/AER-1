#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Pose
from ds4_driver.msg import Status
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import time


##########################################################


class Translator(object):
	def __init__(self):
		#super(Translator, self).__init__()
		## BEGIN_SUB_TUTORIAL setup
		##
		## First initialize `moveit_commander`_ and a `rospy`_ node:
		moveit_commander.roscpp_initialize(sys.argv)
		rospy.init_node('teleop_joystick', anonymous=True)
		self._joystick_subscriber = rospy.Subscriber("status", Status, self.joystick_callback)
		self._last_published_time = rospy.get_rostime()
		## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
		## kinematic model and the robot's current joint states
		self.robot = moveit_commander.RobotCommander()
		self.scene = moveit_commander.PlanningSceneInterface()
		self.group_name = "arm"
		self.move_group = moveit_commander.MoveGroupCommander(self.group_name)
		self._last_published = None
		## Create a `DisplayTrajectory`_ ROS publisher which is used to display
		## trajectories in Rviz:
		self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
		moveit_msgs.msg.DisplayTrajectory,
		queue_size=20)
		self.translated_msg =Pose()
		# self.translated_msg.position.x=0.0
		# self.translated_msg.position.y=0.0
		# self.translated_msg.position.z=0.0
		# self.translated_msg.orientation.x=0.0
		# self.translated_msg.orientation.y=0.0
		# self.translated_msg.orientation.z=0.0
		# self.translated_msg.orientation.w=1.0
		
        
	

	def joystick_callback(self, message):
		# Create message objects
		move_group = self.move_group
		py_flag=message.button_dpad_up
		ny_flag=message.button_dpad_down	
		px_flag=message.button_dpad_right
		nx_flag=message.button_dpad_left
		pz_flag=message.button_l1
		nz_flag=message.button_l2
		###########################
		roll_flag=message.axis_left_x
		#n_roll_flag=message.button_dpad_down	
		pitch_flag=message.axis_left_x
		#n_pitch_flag=message.button_dpad_left
		yaw_flag=message.axis_right_x
		#n_yaw_flag=message.button_l2
		excute_flag=message.button_r2
		x=float(0.0)
		y=float(0.0)
		z=float(0.0)
		roll=float(0.0)
		pitch=float(0.0)
		yaw=float(0.0)
		if px_flag ==1:
			x+=0.01
			#print(self.translated_msg.position.x)
			#print("+x")
		
		if nx_flag ==1:
			x-=0.05
			
		if py_flag ==1:
			y+=0.05
			
		if ny_flag ==1:
			y-=0.05
			
		if pz_flag ==1:
			z+=0.05
			
		if nz_flag ==1:
			z-=0.05
			
		########################################
		if roll_flag >0:
			roll=0.05
			
		if roll_flag <0:
			roll-=0.05
			
		if pitch_flag >0:
			pitch+=0.05
			
		if pitch_flag <0:
			pitch-=0.05
			
		if yaw_flag >0:
			yaw+=0.05
			
		if yaw_flag <0:
			yaw-=0.05
		self.move_group.set_pose_target(self.translated_msg)
		if excute_flag ==1:
			self.excute_goal()
	    #######################################################    
			
		pose_goal = geometry_msgs.msg.Pose()
		pose_goal.position.x = x
		pose_goal.position.y = y
		pose_goal.position.z = z
		pose_goal.orientation.x = roll
		pose_goal.orientation.y = pitch
		pose_goal.orientation.z = yaw
		pose_goal.orientation.w = 1


		move_group.set_pose_target(pose_goal)

		## Now, we call the planner to compute the plan and execute it.
		plan = move_group.go(wait=True)
		# Calling `stop()` ensures that there is no residual movement
		move_group.stop()
		# It is always good to clear your targets after planning with poses.
		# Note: there is no equivalent function for clear_joint_value_targets()
		move_group.clear_pose_targets()
####################################################################################
def main():
	#rospy.init_node('joystick_translator')
	translator = Translator()
	
	while not rospy.is_shutdown():
		rospy.spin()
'''self._last_published = message
self._joystick_publisher.publish()
self.translated_msg = Pose()'''

if __name__ == '__main__':
	main()
	# try:
	# 	tutorial = Translator()
	# 	#tutorial.joystick_callback()
	# except rospy.ROSInterruptException:
	# 	pass