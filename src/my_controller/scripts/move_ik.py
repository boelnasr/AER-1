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


	def go_to_pose_goal(self):
		# Copy class variables to local variables to make the web tutorials more clear.
		# In practice, you should use the class variables directly unless you have a good
		# reason not to.
		move_group = self.move_group

		## BEGIN_SUB_TUTORIAL plan_to_pose
		##
		## Planning to a Pose Goal
		## ^^^^^^^^^^^^^^^^^^^^^^^
		## We can plan a motion for this group to a desired pose for the
		## end-effector:
                pose_goal = geometry_msgs.msg.Pose()
		pose_goal.position.x = 0.4
		pose_goal.position.y = 0.1
		pose_goal.position.z = 0.4
		pose_goal.orientation.w = 1.0
		pose_goal.orientation.x = 0.4
		pose_goal.orientation.y = 0.1
		pose_goal.orientation.z = 0.4


		move_group.set_pose_target(pose_goal)

		## Now, we call the planner to compute the plan and execute it.
		plan = move_group.go(wait=True)
		# Calling `stop()` ensures that there is no residual movement
		move_group.stop()
		# It is always good to clear your targets after planning with poses.
		# Note: there is no equivalent function for clear_joint_value_targets()
		move_group.clear_pose_targets()

if __name__ == '__main__':
	try:
		tutorial = MoveGroupPythonIntefaceTutorial()
		tutorial.go_to_pose_goal()

	except rospy.ROSInterruptException:
		pass
