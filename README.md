# Beyblade Project

Fun project involving the simulation of beyblades in Gazebo. Still ongoing with scope for many interesting developments.

## Objectives ##
1) Look at behaviour of beyblades under ideal conditions (perfectly sharp tip, no air resistance, etc).
2) Look at variation of beyblade behavior with tip geometry and correlate with real-world experience.
3) Attempt to simulate the working of various **mechanisms ("gimmicks")** under different conditions.

## Things done

1. Simple air-resistance model
2. Design beys with different tip geometries in **Fusion360**
3. Test different tip geometries in **Gazebo**
4. **GUI** created using **Tkinter** to launch beys with specific torques at required angles.
5. Created a **simple centrifugal claw mechanism** and tested its working in **Gazebo**.

## Things to do

1. More robust air resistance model 
2. More robust friction model
3. Better GUI (display "bey-state" such as position, angular velocity and other relevant parameters)
4. Improve construction of currently designed mechanisms if possible by incorporating more "science and design" principles.
5. Other Mechanisms -  burst, fangs, absorption, jaw, sagittarius claw, jade jupiter ball bearings, Big Bang Pegasus F:D tip, L-Drago Destructor F:S tip
6. Autonomous detection of ring-out and survivor finish using sensors in simulation
7. Beyblades with sensors to detect other beys - "fighting intent"
8. Vary mass distribution 

## Problems

1. Rotation speed erratic in many launch cases over time
2. Beys do not slow down and stop in a realistic way
3. Friction not working properly (Torsional friction not a function of given tip geometry but needs to be set manually)
4. RTF reduces as number of beys increase



