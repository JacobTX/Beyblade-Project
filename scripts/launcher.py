#!/usr/bin/env python

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

import Tkinter as tk

def launch(T,name,weight):
    rospy.wait_for_service('/gazebo/get_link_state')

    state = rospy.ServiceProxy('/gazebo/get_link_state',GetLinkState)

    S = state(name,'')
    
    a = S.link_state.pose.orientation.x
    b = S.link_state.pose.orientation.y
    c = S.link_state.pose.orientation.z
    d = S.link_state.pose.orientation.w

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

    print(m)

    mx = m[0]
    my = m[1]
    mz = m[2]
   

    rospy.wait_for_service('/gazebo/apply_body_wrench')
    launch = rospy.ServiceProxy('/gazebo/apply_body_wrench',ApplyBodyWrench)

    
    W = Wrench()
    W.force.x = 0
    W.force.y = 0
    W.force.z = weight
    W.torque.x = T * mx
    W.torque.y = T * my
    W.torque.z = T * mz
    
    P = Point()

    launch(name,name,P,W,rospy.Time(1),rospy.Duration(2))
    

def reset(T_val,name,angle,x,y,z,weight):
    rospy.wait_for_service('/gazebo/set_link_state')
    reset = rospy.ServiceProxy('/gazebo/set_link_state',SetLinkState)

    L = LinkState()

    L.link_name=name
    L.pose.position.x = x
    L.pose.position.y = y
    L.pose.position.z = z

    #Quaternion orientation
    theta = (angle * pi)/180.0
    nx = cos(0*pi/180.0)
    ny = sin(0*pi/180.0)
    #nx = 1.0
    #ny = 0.0
    nz = 0.0
    L.pose.orientation.x = nx * sin(theta/2)
    L.pose.orientation.y = ny * sin(theta/2)
    L.pose.orientation.z = nz * sin(theta/2)
    L.pose.orientation.w = cos(theta/2)

    L.reference_frame=''


    reset(L)
    
    launch(T_val,name,weight)
    

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        self.launchButton = tk.Button(self, text='Launch_1',command=self.launch1)            
        self.launchButton.grid(column=1, row=1)  
        self.launchButton.config(height=1,width=10)
        self.launchButton2 = tk.Button(self, text='Launch_2',command=self.launch2)            
        self.launchButton2.grid(column=2, row=1)       
        self.launchButton2.config(height=1,width=10)
        self.launchButton3 = tk.Button(self, text='Launch_3',command=self.launch3)            
        self.launchButton3.grid(column=3, row=1)  
        self.launchButton3.config(height=1,width=10)
        self.launchButton3 = tk.Button(self, text='Launch_4',command=self.launch4)            
        self.launchButton3.grid(column=4, row=1)  
        self.launchButton3.config(height=1,width=10)  
        self.launchButton4 = tk.Button(self, text='Launch_5',command=self.launch5)            
        self.launchButton4.grid(column=5, row=1)  
        self.launchButton4.config(height=1,width=10)  
        self.text1 = tk.Text(self)
        self.text1.grid(column=1,row=100)
        self.text1.config(height=1,width=10)
        self.text2 = tk.Text(self)
        self.text2.grid(column=2,row=100)
        self.text2.config(height=1,width=10)
        self.text3 = tk.Text(self)
        self.text3.grid(column=3,row=100)
        self.text3.config(height=1,width=10)
        self.text4 = tk.Text(self)
        self.text4.grid(column=1,row=200)
        self.text4.config(height=1,width=10)
        self.text5 = tk.Text(self)
        self.text5.grid(column=2,row=200)
        self.text5.config(height=1,width=10)
        self.text6 = tk.Text(self)
        self.text6.grid(column=3,row=200)
        self.text6.config(height=1,width=10)
        self.text7 = tk.Text(self)
        self.text7.grid(column=4,row=100)
        self.text7.config(height=1,width=10)
        self.text8 = tk.Text(self)
        self.text8.grid(column=4,row=200)
        self.text8.config(height=1,width=10)
        self.text9 = tk.Text(self)
        self.text9.grid(column=5,row=100)
        self.text9.config(height=1,width=10)
        self.text10 = tk.Text(self)
        self.text10.grid(column=5,row=200)
        self.text10.config(height=1,width=10)

    def launch1(self):
        #T_val = float(raw_input("Enter torque:"))
        #angle_1 = float(raw_input("Enter angle:"))
        T_val = float(self.text1.get("1.0",'end-1c'))
        angle_1 = float(self.text4.get("1.0",'end-1c'))
        reset(T_val,'beyblade::link_0',angle_1,0.0,0.5,1.0,10.0)    

    def launch2(self):
        #T_val_2 = float(raw_input("Enter torque:"))
        #angle_2 = float(raw_input("Enter angle:"))
        T_val_2 = float(self.text2.get("1.0",'end-1c'))
        angle_2 = float(self.text5.get("1.0",'end-1c'))
        reset(T_val_2,'beyblade2::link_0',angle_2,-0.5,0,1.0,10.0)

    def launch3(self):
        #T_val_3 = float(raw_input("Enter torque:"))
        #angle_3 = float(raw_input("Enter angle:"))
        T_val_3 = float(self.text3.get("1.0",'end-1c'))
        angle_3 = float(self.text6.get("1.0",'end-1c'))
        reset(T_val_3,'beyblade3::link_0',angle_3,0.5,0,1.0,10.0)

    def launch4(self):
        #T_val_3 = float(raw_input("Enter torque:"))
        #angle_3 = float(raw_input("Enter angle:"))
        T_val_4 = float(self.text7.get("1.0",'end-1c'))
        angle_4 = float(self.text8.get("1.0",'end-1c'))
        reset(T_val_4,'beyblade4::link_0',angle_4,0.0,-0.5,1.0,10.0)
        
    def launch5(self): 
        T_val_5 =   float(self.text9.get("1.0",'end-1c'))
        angle_5 =   float(self.text10.get("1.0",'end-1c')) 
        reset(T_val_5,'lion_claw::base_link',angle_5,0.0,0.0,1.0,5.0)



    

if __name__=="__main__":

    app = Application()                       
    app.master.title('Launcher interface')    
    app.mainloop() 
