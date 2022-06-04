# Beyblade Project

Fun project involving the simulation of beyblades in Gazebo. Still ongoing with scope for many interesting developments.

## Objectives ##
1) Look at behaviour of beyblades under ideal conditions (perfectly sharp tip, no air resistance, etc).
2) Look at variation of beyblade behavior with tip geometry and correlate with real-world experience.

## Things done

1. Simple air-resistance model
2. Design beys with different tip geometries in **Fusion360**
3. Test different tip geometries in **Gazebo**
4. **GUI** created using **Tkinter** to launch beys with specific torques at required angles. 

## Things to do

1. More robust air resistance model 
2. More robust friction model
3. Better GUI
4. Mechanisms - centrifugal blades, sword, burst, fangs, absorption, jaw
5. Autonomous detection of ring-out and survivor finish using sensors in simulation
6. Beyblades with sensors to detect other beys - "fighting intent"
7. Vary mass distribution 

## Problems

1. Rotation speed erratic in many launch cases over time
2. Beys do not slow down and stop in a realistic way
3. Friction not working properly (Torsional friction not a function of given tip geometry but needs to be set manually)
4. RTF reduces as number of beys increase



