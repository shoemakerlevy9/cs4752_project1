#!/usr/bin/env python
import rospy
import baxter_interface
from std_msgs.msg import String
from hpb_proj1.msg import State
from hpb_proj1.srv import move_robot


rospy.init_node('controller', anonymous=True)

currentState = 0

def scatter(prevState):
    if prevState == "stack_asc":
        

def handleCommand(cmd):
    if cmd == "scatter":
        pass
    elif cmd == "stack_asc":
        pass
    elif cmd == "stack_desc":
        pass
    
    

#    if cmd==currentState
   
def handleState(data):
    if data.descript == 'stack_asc':
        end_state=1
    elif data.descript == 'stack_des':
        end_state=2
    elif data.descript == 'scattered':
        end_state=3
    else:
        end_state=0 #uninitialized
    
    #if state == end_state:
     #   return
    #else:
    #    move_robot("open gripper", 1)  
    
#def move_robot_server():
    #rospy.Service('move_robot', hbp_proj1.srv.move_robot, add_two_ints)
 
# Service that sends requests to the 'robot_interface' server
def move_robot(action, target):           
    rospy.init_node('move_robot', anonymous=True)
    rospy.service(action, target)

def controller():
    rospy.Subscriber("state", State, handleState)
    rospy.Subscriber("command", String, handleCommand)
    #action()
    rospy.spin()

if __name__ == '__main__':
    controller()
