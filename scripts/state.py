#! /usr/bin/env python

import rospy
import random
import numpy as np
from math import sin,cos,acos,pi
from gazebo_msgs.srv import ApplyBodyWrench
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import Point
from gazebo_msgs.srv import SetLinkState
from gazebo_msgs.msg import LinkState
from gazebo_msgs.srv import GetLinkState
from std_msgs.msg import Float32MultiArray

class bey_state:

    def __init__(self):
        rospy.init_node("bey_state")
        self.P = rospy.Publisher("bey_state",Float32MultiArray,queue_size=100)

        rospy.Timer(rospy.Duration(1.0/10),self.pub)

        rospy.spin()

    def pub(self,event=None):
        rospy.wait_for_service('/gazebo/get_link_state')

        state = rospy.ServiceProxy('/gazebo/get_link_state',GetLinkState)

        S2 = state('beyblade::link_0','')
        S3 = state('beyblade2::link_0','')

        wx = S2.link_state.twist.angular.x
        wy = S2.link_state.twist.angular.y
        wz = S2.link_state.twist.angular.z

        ux = S3.link_state.twist.angular.x
        uy = S3.link_state.twist.angular.y
        uz = S3.link_state.twist.angular.z 

        W = Float32MultiArray()
        W.data=[wx,wy,wz,ux,uy,uz]
        self.P.publish(W)


if __name__=="__main__":
    B = bey_state()

