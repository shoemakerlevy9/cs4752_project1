#!/user/bin/env python

PACKAGE='youpuntedbaxter_proj1'

from State.msg import State
from robot_interface.srv import move_robot
import rospy

# Publishes the state of the world to the topic "/state" at a rate of 1 Hz
pub = rospy.Publisher('state', state, queue_size = 10) 
rospy.init_node('robot_interaface', anonymous=True)
rate = rospy.Rate(1)

# Subscribes to move_robot
rospy.intit_node('robot_interface', anonymous=True)
rospy.Subscriber("move_robot",moverobot, callback)

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

int stacks[5]

#Creates an array of blocks. For this problem we have block1 block2 and block3.
blocks = []
blocks.append(block("block1", 0, 1))
blocks.append(block("block2", 0, 1))
blocks.append(block("block3", 0, 1))
blocks.append(block("table", 0, 0))
blocks.append(block("table", 1, 0))
blocks.append(block("table", 2, 0))
blocks.append(block("table", 3, 0))
blocks.append(block("table", 4, 0))

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

rospy.spin()
