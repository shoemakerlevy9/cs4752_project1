#!/usr/bin/env python
import rospy
import baxter_interface
from std_msgs.msg import String
from hpb_proj1.msg import State
from hpb_proj1.srv import Move_Robot

rospy.init_node('controller', anonymous=True)
rospy.Service('move_robot', Move_Robot, move_robot)

def callback(data):
    if data.descript == 'stack_asc':
        state=1
    elif data.descript == 'stack_des':
        state=2
    elif data.descript == 'scattered':
        state=3
    else:
        state=0 #uninitialized
    return state 
   
def callback2():
    if data.descript == 'stack_asc':
        end_state=1
    elif data.descript == 'stack_des':
        end_state=2
    elif data.descript == 'scattered':
        end_state=3
    else:
        end_state=0 #uninitialized
    
    if state == end_state:
        return
    else:
        move_robot("open gripper", 1)  
    
#def move_robot_server():
    #rospy.Service('move_robot', hbp_proj1.srv.move_robot, add_two_ints)
 
# Service that sends requests to the 'robot_interface' server
def move_robot(action, target):           
    rospy.init_node('move_robot', anonymous=True)
    rospy.service(action, target)

def controller():
    rospy.Subscriber("state", State, callback)
    rospy.Subscriber("command", String, callback2)
    #action()
    rospy.spin()

if __name__ == '__main__':
    controller()
