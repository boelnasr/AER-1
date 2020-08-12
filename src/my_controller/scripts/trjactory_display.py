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

def all_close(goal, actual, tolerance):
  """
  Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
  @param: goal       A list of floats, a Pose or a PoseStamped
  @param: actual     A list of floats, a Pose or a PoseStamped
  @param: tolerance  A float
  @returns: bool
  """
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

  return True

class MoveGroupPythonIntefaceTutorial(object):
	def __init__(self):
		super(MoveGroupPythonIntefaceTutorial, self).__init__()

		## BEGIN_SUB_TUTORIAL setup
		##
		## First initialize `moveit_commander`_ and a `rospy`_ node:
		moveit_commander.roscpp_initialize(sys.argv)
		rospy.init_node('display_trjactory', anonymous=True)

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
	def plan_cartesian_path(self, scale=1):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.
		group=self.move_group

		## BEGIN_SUB_TUTORIAL plan_cartesian_path
		##
		## Cartesian Paths
		## ^^^^^^^^^^^^^^^
		## You can plan a Cartesian path directly by specifying a list of waypoints
		## for the end-effector to go through:
		##
		
		waypoints = []
		
		wpose = group.get_current_pose().pose
		wpose.position.z -= scale * 0.3  # First move up (z)
		wpose.position.y += scale * 0.2  # and sideways (y)
		waypoints.append(copy.deepcopy(wpose))

		wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
		waypoints.append(copy.deepcopy(wpose))

		wpose.position.y -= scale * 0.1  # Third move sideways (y)
		waypoints.append(copy.deepcopy(wpose))

		# We want the Cartesian path to be interpolated at a resolution of 1 cm
		# which is why we will specify 0.01 as the eef_step in Cartesian
		# translation.  We will disable the jump threshold by setting it to 0.0 disabling:
		(plan, fraction) = group.compute_cartesian_path(
										waypoints,   # waypoints to follow
										0.01,        # eef_step
										0.0)         # jump_threshold
		print(waypoints)

		# Note: We are just planning, not asking move_group to actually move the robot yet:
		return plan, fraction

		## END_SUB_TUTORIAL

	def display_trajectory(self, plan):
		# Copy class variables to local variables to make the web tutorials more clear.
		# In practice, you should use the class variables directly unless you have a good
		# reason not to.
		robot = self.robot
		display_trajectory_publisher = self.display_trajectory_publisher

		## BEGIN_SUB_TUTORIAL display_trajectory
		##
		## Displaying a Trajectory
		## ^^^^^^^^^^^^^^^^^^^^^^^
		## You can ask RViz to visualize a plan (aka trajectory) for you. But the
		## group.plan() method does this automatically so this is not that useful
		## here (it just displays the same trajectory again):
		##
		## A `DisplayTrajectory`_ msg has two primary fields, trajectory_start and trajectory.
		## We populate the trajectory_start with our current robot state to copy over
		## any AttachedCollisionObjects and add our plan to the trajectory.
		display_trajectory = moveit_msgs.msg.DisplayTrajectory()
		display_trajectory.trajectory_start = robot.get_current_state()
		display_trajectory.trajectory.append(plan)
		# Publish
		display_trajectory_publisher.publish(display_trajectory)

		## END_SUB_TUTORIAL



if __name__ == '__main__':
	try:
		tutorial = MoveGroupPythonIntefaceTutorial()
		cartesian_plan, fraction = tutorial.plan_cartesian_path()
		tutorial.display_trajectory(cartesian_plan)
		tutorial.execute_plan(cartesian_plan)

	except rospy.ROSInterruptException:
		pass
