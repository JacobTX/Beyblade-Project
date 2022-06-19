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
from std_msgs.msg import String

class air_drag:

    def __init__(self, name):
        rospy.init_node("air_drag_exerter")

        self.name = name
       
        rospy.Timer(rospy.Duration(1.0/100.0),self.exert)

    def exert(self,event=None):
        rospy.wait_for_service('/gazebo/get_link_state')

        state = rospy.ServiceProxy('/gazebo/get_link_state',GetLinkState)

        S2 = state(self.name,'')

        a = S2.link_state.pose.orientation.x
        b = S2.link_state.pose.orientation.y
        c = S2.link_state.pose.orientation.z
        d = S2.link_state.pose.orientation.w
        wx = S2.link_state.twist.angular.x
        wy = S2.link_state.twist.angular.y
        wz = S2.link_state.twist.angular.z

        theta = 2 * acos(d)
        if (theta >= 0) and (theta < pi):
            s = 1
        elif (theta >= pi) and (theta < 2*pi):
            s = -1

        lx = s*a /(1-d**2)**0.5
        ly = s*b /(1-d**2)**0.5
        lz = s*c /(1-d**2)**0.5 

        l = np.array([lx,ly,lz])
        n = np.array([0,0,1])

        m = cos(theta)*n + (sin(theta))*np.cross(l,n) + (1-cos(theta))*np.dot(l,n)*l


        mx = m[0]
        my = m[1]
        mz = m[2]
    

        rospy.wait_for_service('/gazebo/apply_body_wrench')
        drag = rospy.ServiceProxy('/gazebo/apply_body_wrench',ApplyBodyWrench)

        k = 1.0/500
        T = -(wz/abs(wz))*k*(wz)**2
        
        W = Wrench()
        W.force.x = 0
        W.force.y = 0
        W.force.z = 0
        W.torque.x = T * mx
        W.torque.y = T * my
        W.torque.z = T * mz
        
        P = Point()

        drag(self.name,self.name,P,W,rospy.Time(1),rospy.Duration(1.0/100))

       

def exert():
    A = air_drag('beyblade::link_0')
    B = air_drag('beyblade2::link_0')
    rospy.spin()


if __name__=="__main__":
    exert()
