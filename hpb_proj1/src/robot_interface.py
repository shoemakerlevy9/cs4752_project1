#!/usr/bin/env python

PACKAGE='hpb_proj1'

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from hpb_proj1.msg import State

#rospy.Service('move_robot', move_robot, handle_moveRobot)

#from robot_interface.srv import move_robot
current_state = State()
current_state.descript = "hello"
current_state.r1 = [5,5]
current_state.b1 = [5,5]
current_state.b2 = [5,5]
current_state.b3 = [5,5]
descript = "hi"
r1 = [5,5]
b1 = [5,5]
b2 = [5,5]
b3 = [5,5]


def talker():
    #current_state = init_state()
    pub = rospy.Publisher('state', State, queue_size=10)
    rospy.init_node('robot_interface', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        rospy.loginfo("here")
        pub.publish(descript,r1,b1,b2,b3)
        rate.sleep()

def init_state():
    #Get initial number of blocks set in launch file 
    num_blocks = rospy.get_param('/num_blocks')
    #Get initial configuration set in launch file (ascending or descending) 
    config = rospy.get_param('/configuration')
    #
    state.descript = "stack_asc"
    state.r1 = [0,4]
    state.b1 = [0,1]
    state.b1 = [0,2]
    state.b1 = [0,3]
    return r1
    #Inizialize blocks accourding to the configuration parameter
    try:
        if config == "stack_asc":
            state = stack_asc(num_blocks)
        elif config == "stack_des":
            state = stack_des(num_blocks)
    except ValueError:
        print '/configuration is an invalid parameter', config

def stack_asc(num_blocks):
    #TODO make this dyanamicly initialize b1-bn
    #stack the blocks in position X=0 in ascending order
    b1 = [0,3]
    b2 = [0,2]
    b3 = [0,1]

def stack_des(num_blocks):
    #TODO make this dyanamicly initialize b1-bn
    #stack the blocks in position X=0 in descending order
    b3 = [0,3]
    b2 = [0,2]
    b1 = [0,1]


#def update_word(move_robot):
 #   if mov_robot.req.Action = "Open Gripper":
#        baxter.gripper = "open"
#        return True  
#    elif mov_robot.req.Action = "Close Gripper":
 #       baxter.gripper = "closed"
#        return True

def update_state(action, target):
    try:    
        if action == "open gripper":
            b1 = [0,9] #filler code
            return True
    except:
        return False
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

# x - X position of robot
# z - Z Position of Robot
# gripper - State of robots gripper ("Open"/"Closed")
# held_block - Name of the block being held by the gripper ("none" if no block is being held)

#class robot
#	def __ ini__(self, x, z, gripper, held_block)
#		self.x = x
#		self.z = z
#		self.gripper = gripper
#		self.held_block = held_block


'''
# name - Name of the block (e.g. "block1" "block2" ...)
# x - X position of th block
# z - Z position of the block
class block:
	def __init__(self,name, x, z)
		self.name = name
		self.x = x
		self.z = z
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
