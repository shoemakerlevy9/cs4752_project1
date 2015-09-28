#!/usr/bin/env python

PACKAGE='hpb_proj1'

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from hpb_proj1.msg import State
from hpb_proj1.srv import move_robot
from Block import Block



#from robot_interface.srv import move_robot
class RobotInterface(object):
	"""maintains the following instance variables
	curState
		descript
		blockRepr
		r1
	blockLookup
	num_blocks
	"""
	def __init__(self):
		rospy.Service('move_robot', move_robot, self.handle_moveRobot)
		self.init_state()
		pub = rospy.Publisher('state', State, queue_size=10)
		rospy.init_node('robot_interface', anonymous=True)
		rate = rospy.Rate(1) # 1hz
		while not rospy.is_shutdown():
		    pub.publish(self.curState)
		    rate.sleep()

	def handle_moveRobot(s,req):
		#req.Action #<-- string
		#req.Target #<-- int
		action = req.Action
		if action == "moveTo":
		    if s.gState == 0:
 				return False
		    tBlock = s.blockLookup[req.Target]
		    s.blockInGripper = req.Target
		    s.curState.r1 = [tBlock.x,tBlock.z,s.gState]
		elif action == "moveAbove": #BUG: will place 2 blocks in the same location
		    tBlock = s.blockLookup[req.Target]
		    if s.blockHeld != 0:
 				s.blockLookup[s.blockHeld].x = tBlock.x
 				s.blockLookup[s.blockHeld].z = tBlock.z+1
		    s.curState.r1 = [tBlock.x,tBlock.z+1,s.gState]
		elif action == "closeGripper":
		    s.gState = 0
		    s.blockHeld = s.blockInGripper
		    s.curState.r1[2] = 0

		elif action == "openGripper":
		    s.gState = 1
		    s.curState.r1[2] = 1
		    s.blockHeld = 0
		else:
		    return False
		s.curState.blockRepr = repr(s.blockLookup)
		s.curState.descript = action #TODO this is not working
		return True

	def init_state(self):
		self.blockHeld = 0
		self.gState = 1
		self.num_blocks = rospy.get_param('/num_blocks')
		self.config = rospy.get_param('/configuration')
		self.num_arms = rospy.get_param('/num_arms')
		self.blockInGripper = self.num_blocks
		self.curState = State()
		self.curState.descript = self.config
		self.curState.r1 = [1,self.num_blocks,1]
		if self.config == "stack_asc":
			self.stack_asc()
		elif self.config == "stack_des":
			self.stack_asc()
		else:
			print 'configuration is an invalid parameter', config
		self.curState.blockRepr = repr(self.blockLookup)

	def stack_asc(s):
	    #TODO make this dyanamicly initialize b1-bn
	    #stack the blocks in position X=0 in ascending order
		s.blockLookup = {}
		for i in range(1,s.num_blocks+1):
			s.blockLookup[i] = Block(i,1,i)
			s.blockLookup[-i] = Block(-i,i,0)

	def stack_des(s):
	    #TODO make this dyanamicly initialize b1-bn
	    #stack the blocks in position X=0 in descending order
	    s.blockLookup = {}
	    for i in range(1,s.num_blocks+1):
			s.blockLookup[i] = Block(i,1,num_blocks-i)
			s.blockLookup[-i] = Block(-i,i,0)


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
        RobotInterface()
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
