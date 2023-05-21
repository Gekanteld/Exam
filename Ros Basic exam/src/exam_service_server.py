#! /usr/bin/env python

import math
import rospy
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class huskyeyes ():
    def __init__(self):
        self.serv = rospy.Service('/crash_direction_service', Trigger,self.callback)
        self.sub = rospy.Subscriber("/scan",LaserScan,self.subcallback)
        
    def subcallback(self, submsg):
        laserhold = submsg.ranges
        self.Right = laserhold[0]
        self.Front = laserhold[360]
        self.Left = laserhold[719]

    def callback(self, msg):
        response = TriggerResponse()
        
        if self.Right > self.Left and self.Right > self.Front:
            # move Right
            response.message = "right"
        elif self.Front > self.Left and self.Front > self.Right:
            # move Front
            response.message = "front"
        else:
            # move left
            response.message = "left"

        rospy.loginfo ('front: %s, left: %s right: %s' ,self.Front, self.Left, self.Right)
       
        response.success = True
        return response
             
    
if __name__ == "__main__":
    rospy.init_node('service_server')
    huskyeyes()
    rospy.spin()


# this service server, when called, must provide the direction to move.

# the service must use the Trigger service message

# the service response must return one of the following words: front, left or right

# this service itself should not move the robot
