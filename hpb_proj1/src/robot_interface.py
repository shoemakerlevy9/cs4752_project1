#!/usr/bin/env python

PACKAGE='hpb_proj1'

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from hpb_proj1.msg import State

#from robot_interface.srv import move_robot

current_state = "scrambled"
r1 = [0,4]
b1 = [0,1]
b2 = [0,2]
b3 = [0,3]


def talker():
    pub = rospy.Publisher('state', State, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        pub.publish(current_state,r1,b1,b2,b3)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

'''

# name - Name of the block (e.g. "block1" "block2" ...)
# x - X position of th block
# z - Z position of the block
class block:
	def __init__(self,name, x, z)
		self.name = name
		self.x = x
		self.z = z

# x - X position of robot
# z - Z Position of Robot
# gripper - State of robots gripper ("Open"/"Closed")
# held_block - Name of the block being held by the gripper ("none" if no block is being held)
class robot
	def __ ini__(self, x, z, gripper, held_block)
		self.x = x
		self.z = z
		self.gripper = gripper
		self.held_block = held_block
'''


'''
#Creates baxter and initializes him at a certain location
baxter = robot(0,4)

#2D array that stores a 0 for open air, a 1 for table, and a 2 for a block.
World = [[0 for x in range(5)] for x in range(5)] 


def blockPresent()
	if baxter.x = block.x
		if baxter.z = block.z
			return True
	else
		return false


def callback (move_robot):
	#If baxter is above a block and his gripper is open he will move down to that blocks position
	#If he is over a block but his gripper is closed he will run into the block and stop 1 unit shy
	#If he is not over a block he will print "No block detected"
	if move_robot = "move to block":
		if baxter.gripper = "closed":
			baxter.z = stacks[baxter.z]+1
			print("baxter crashed")
		if baxter.gripper = "open":
			baxter.z = stacks[baxter.z]

	
	if move_robot = "close gripper": 
		baxter.gripper = "closed"
		if block_present():
			baxter.held_block = block1

	if move_robot = "open gripper":
		baxter.gripper = "open"
	
	if move_robot = "move above block":
		baxter.y = 1 
		baxter.z = stack1_h
'''
