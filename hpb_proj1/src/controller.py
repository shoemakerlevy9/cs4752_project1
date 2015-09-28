#!/usr/bin/env python
import rospy
import baxter_interface
from std_msgs.msg import String
from hpb_proj1.msg import State
from hpb_proj1.srv import move_robot
from Block import Block


rospy.init_node('controller', anonymous=True)
moveRobot = rospy.ServiceProxy('move_robot', move_robot)
blockLookup = {}
r1 = [0,0]
descript = ""
busy = 0

def scatter():
	stackX = findStack()
	block = getHighestBlock(stackX)
	locationAdd = 0
	for i in range(1,block.z):
		block = getHighestBlock(stackX)
		if i == stackX:
			locationAdd = 1
		rospy.loginfo(block)
		moveRobot("moveTo",block.name)
		rospy.sleep(.5)
		moveRobot("closeGripper",0)
		rospy.sleep(.5)
		moveRobot("moveAbove",-(i+locationAdd))
		rospy.sleep(.5)
		moveRobot("openGripper",0)
		rospy.sleep(.5)

def stack_des():
	num_blocks = rospy.get_param('/num_blocks')
	for i in range(1,num_blocks):
		moveRobot("moveTo", num_blocks-i)
		rospy.sleep(.5)
		moveRobot("closeGripper",0)
		rospy.sleep(.5)
		moveRobot("moveAbove", num_blocks-i+1)
		rospy.sleep(.5)
		moveRobot("openGripper",0)
	
def stack_asc():
	num_blocks = rospy.get_param('/num_blocks')
	for i in range(1,num_blocks):
		moveRobot("moveTo", i+1)
		rospy.sleep(.5)
		moveRobot("closeGripper",0)
		rospy.sleep(.5)
		moveRobot("moveAbove", i)
		rospy.sleep(.5)
		moveRobot("openGripper",0)

def findStack():
	for block in blockLookup.values():
		if block.z > 0:
			return block.x

def getHighestBlock(position):
	highestBlock = None
	highestInd = -1
	for block in blockLookup.values():
		if block.x == position and block.z > highestInd:
			highestBlock = block
			highestInd = block.z
	return highestBlock

def handleCommand(command):
    global busy
    cmd = command.data
    if cmd == "scatter":
        if busy == 0:
            busy = 1
            scatter()
            busy = 0
                
                
    elif cmd == "stack_asc":
        if busy == 0:
            busy = 1
            scatter()
            stack_asc()
            busy = 0

    elif cmd == "stack_desc":
        if busy == 0:
            busy = 1
            scatter()
            stack_des()
            busy = 0
    
    

#    if cmd==currentState
   
def handleState(data):
    global blockLookup
    global r1
    global descript
    blockLookup = eval(data.blockRepr)
    r1 = data.r1
    descript = data.descript

# Service that sends requests to the 'robot_interface' server

def controller():
    rospy.Subscriber("state", State, handleState)
    rospy.Subscriber("command", String, handleCommand)
    #action()
    rospy.spin()

if __name__ == '__main__':
    controller()
