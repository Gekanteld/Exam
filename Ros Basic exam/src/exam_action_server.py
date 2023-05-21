#! /usr/bin/env python

import rospy
import actionlib
from basics_exam.msg import record_odomResult, record_odomAction

class action_server():
    def __init__(self):
        self.action_server = actionlib.SimpleActionServer("/rec_odom_as", record_odomAction, self.messi, False)
        self.action_server.start()
        self.result = record_odomResult()
        self.rate = rospy.Rate(1)

    def messi(self, goalvar):
        if self.action_server.is_preempt_requested():
            self.action_server.set_preemped()
        
        for i in range(20):
            if self.action_server.is_preempt_requested():
                self.action_server.set_preemped()
                break
        
            self.rate.sleep()
            i+=1
        rospy.loginfo("action succeeded")    
        self.action_server.set_succeeded(self.result)

if __name__ == "__main__":
    rospy.init_node('action_program')
    action_server()
    rospy.spin()

# Goal: No goal is sent, just an empty message indicating that the action server must start

# Feedback: No feedback must be provided

# Result: After 60 seconds, it will provide the whole list of positions
