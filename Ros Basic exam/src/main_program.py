#! /usr/bin/env python

import rospy
import time
import actionlib
from geometry_msgs.msg import Twist
from basics_exam.msg import record_odomAction, record_odomActionGoal, record_odomActionFeedback, record_odomActionResult
from std_srvs.srv import Trigger, TriggerRequest

def pluto_vooruit(tijd):
    rospy.loginfo("vooruit")
    pluto_uitlaten.angular.z = 0
    pluto_uitlaten.linear.x = 0.5
    while True:
        pluto_publisher.publish (pluto_uitlaten)
        print("rijden")
    time.sleep(tijd)
    

def pluto_rechts(tijd):
    rospy.loginfo("rechts")
    pluto_uitlaten.angular.z = 1
    pluto_uitlaten.linear.x = 0
    pluto_publisher.publish (pluto_uitlaten)
    time.sleep(1)

    pluto_uitlaten.angular.z = 0
    pluto_uitlaten.linear.x = 0.5
    pluto_publisher.publish (pluto_uitlaten)
    time.sleep(tijd)

def pluto_links(tijd):
    rospy.loginfo("links")
    pluto_uitlaten.angular.z = -1
    pluto_uitlaten.linear.x = 0
    pluto_publisher.publish (pluto_uitlaten)
    time.sleep(1)

    pluto_uitlaten.angular.z = 0
    pluto_uitlaten.linear.x = 0.5
    pluto_publisher.publish (pluto_uitlaten)
    time.sleep(tijd)

rospy.init_node("main_program")
pluto_uitlaten = Twist()
pluto_publisher = rospy.Publisher("/cmd_vel",Twist, queue_size=1)
actionclient = actionlib.SimpleActionClient("/rec_odom_as",record_odomAction)

rospy.wait_for_service("/crash_direction_service")

husky_service = rospy.ServiceProxy("/crash_direction_service", Trigger)

husky_request = TriggerRequest()

actionclient.wait_for_server()
service_result = husky_service(husky_request)

if service_result.message =="front":
    pluto_vooruit(10)
elif service_result.message=="right":
    pluto_rechts(10)
else:
    pluto_links(10)

pluto_uitlaten.angular.z = 0
pluto_uitlaten.linear.x = 0
pluto_publisher.publish (pluto_uitlaten)
print ("pluto is freeeeee!")




# Call the action server so that when the robot starts trying to get out of the room it will storeg all of the positions that the robot has visited

# Call the service in order to know which is the next direction it has to move in

# Move the robot in the specified direction

# When the minute has passed, the robot must stop and end everything

# When the robot is out of the room, it must print a message indicating it has gone out
