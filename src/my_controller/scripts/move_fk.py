#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from math import radians

class MoveGroupPythonIntefaceTutorial(object):
	def __init__(self):
		super(MoveGroupPythonIntefaceTutorial, self).__init__()

		## BEGIN_SUB_TUTORIAL setup
		##
		## First initialize `moveit_commander`_ and a `rospy`_ node:
		moveit_commander.roscpp_initialize(sys.argv)
		rospy.init_node('move_ik', anonymous=True)

		## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
		## kinematic model and the robot's current joint states
		robot = moveit_commander.RobotCommander()

		## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
		## for getting, setting, and updating the robot's internal understanding of the
		## surrounding world:
		scene = moveit_commander.PlanningSceneInterface()

		## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
		## to a planning group (group of joints).  In this tutorial the group is the primary
		## arm joints in the Panda robot, so we set the group's name to "panda_arm".
		## If you are using a different robot, change this value to the name of your robot
		## arm planning group.
		## This interface can be used to plan and execute motions:
		group_name = "arm"
		self.move_group = moveit_commander.MoveGroupCommander(group_name)

		## Create a `DisplayTrajectory`_ ROS publisher which is used to display
		## trajectories in Rviz:
		self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
		moveit_msgs.msg.DisplayTrajectory,
		queue_size=20)


	def go_to_joints_goal(self):
		# Copy class variables to local variables to make the web tutorials more clear.
		# In practice, you should use the class variables directly unless you have a good
		# reason not to.
		print("=========Enter Joints values in degres")
		theta=[0]*6
		theta[0]=input("Enter theta one value: ")
		theta[1]=input("Enter theta teo value: ")
		theta[2]=input("Enter theta three value: ")
		theta[3]=input("Enter theta four value: ")
		theta[4]=input("Enter theta five value: ")
		theta[5]=input("Enter theta six value: ")
		move_group = self.move_group

		# Copy class variables to local variables to make the web tutorials more clear.
		# In practice, you should use the class variables directly unless you have a good
		# reason not to.
		## BEGIN_SUB_TUTORIAL plan_to_joint_state
		##
		## Planning to a Joint Goal
		## ^^^^^^^^^^^^^^^^^^^^^^^^
		## The Panda's zero configuration is at a `singularity <https://www.quora.com/Robotics-What-is-meant-by-kinematic-singularity>`_ so the first
		## thing we want to do is move it to a slightly better configuration.
		# We can get the joint values from the group and adjust some of the values:
		joint_goal = self.move_group.get_current_joint_values()
		joint_goal[0] = radians(theta[0])
		joint_goal[1] = radians(theta[1])
		joint_goal[2] = radians(theta[2])
		joint_goal[3] = radians(theta[3])
		joint_goal[4] = radians(theta[3])
		joint_goal[5] = radians(theta[5])
		
		# The go command can be called with joint values, poses, or without any
		# parameters if you have already set the pose or joint target for the group
 		self.move_group.go(joint_goal, wait=True)

		# Calling ``stop()`` ensures that there is no residual movement
		self.move_group.stop()

		## END_SUB_TUTORIAL

		# For testing:
		# Note that since this section of code will not be included in the tutorials
		# we use the class variable rather than the copied state variable
		current_joints = self.move_group.get_current_joint_values()
        #return all_close(joint_goal, current_joints, 0.01)

if __name__ == '__main__':
	try:
		tutorial = MoveGroupPythonIntefaceTutorial()
		tutorial.go_to_joints_goal()

	except rospy.ROSInterruptException:
		pass
