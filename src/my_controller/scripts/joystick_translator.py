#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from gazebo_msgs import ModelState

AXIS_1 = 0
AXIS_2 = 5

SQUARE = 0
CROSS = 1
CIRCLE = 2
TRIANGLE = 3
L1 = 4
R1 = 5
L2 = 6
R2 = 7


class Translator(QtWidgets.QWidget):
	def __init__(self):
		self._joystick_subscriber = rospy.Subscribers("joy", Joy, self.joystick_callback)
		self._joystick_publisher = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)
		self._last_published_time = rospy.get_rostime()
		self._last_published = None
		self.timer = rospy.Timer(rospy.Duration(1./20.), self.timer_callback)
        
	def timer_callback(self, event):
		if self._last_published and self._last_published_time < rospy.get_rostime() + rospy.Duration(1.0/20.):
			self.joystick_callback(self._last_published)

	def joystick_callback(self, message):
		# Create message objects
		model_state = ModelState()

		model_state = "robot"

		if message.axis[] >= 0:
			# Do something
		else:
			# Do something else

		if message.buttons[]:
			# Do something
		else:
			# Do something else


		self._last_published = message
		self._joystick_publisher.publish(model_state)


def main():
	rospy.init_node('joy_translator')
	translator = Translator()

	while not rospy.is_shutdown():
		rospy.spin()
	

if __name__ == '__main__':
	main()

