#!/usr/bin/env python

PACKAGE='hpb_proj1'

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from hpb_proj1.msg import State
from hpb_proj1.srv import move_robot

#rospy.Service('move_robot', move_robot, handle_moveRobot)

#from robot_interface.srv import move_robot

    
def handle_moveRobot(req):
    #req.Action #<-- string
    #req.Target #<-- int
    return True

blocks = {}

def talker():
    rospy.Service('move_robot', move_robot, handle_moveRobot)
    current_state = init_state()
    pub = rospy.Publisher('state', State, queue_size=10)
    rospy.init_node('robot_interface', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        pub.publish(current_state)
        rate.sleep()

def init_state():
    #Get initial number of blocks set in launch file 
    num_blocks = rospy.get_param('/num_blocks')
    #Get initial configuration set in launch file (ascending or descending) 
    config = rospy.get_param('/configuration')
    #
    state = State()
    state.descript = config
    state.r1 = [0,4]
    #state.b1 = [0,1]
    #state.b2 = [0,2]
    #state.b3 = [0,3]
    #return state
    #Inizialize blocks accourding to the configuration parameter
    try:
        if config == "stack_asc":
            return stack_asc(state,num_blocks)
        elif config == "stack_des":
            return stack_des(state,num_blocks)
    except ValueError:
        print '/configuration is an invalid parameter', config

def stack_asc(state,num_blocks):
    #TODO make this dyanamicly initialize b1-bn
    #stack the blocks in position X=0 in ascending order
    state.b1 = [0,3]
    state.b2 = [0,2]
    state.b3 = [0,1]
    return state

def stack_des(state,num_blocks):
    #TODO make this dyanamicly initialize b1-bn
    #stack the blocks in position X=0 in descending order
    state.b3 = [0,3]
    state.b2 = [0,2]
    state.b1 = [0,1]
    return state


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



# name - Name of the block (e.g. "block1" "block2" ...)
# x - X position of th block
# z - Z position of the block
class Block:
	def __init__(self,name, x, z):
		self.name = name
		self.x = x
		self.z = z

    def __repr__(self):
        return "Block(%s,%d,%d)"%(self.name,self.x,self.z)



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
