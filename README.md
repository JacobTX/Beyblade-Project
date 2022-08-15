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
5. Created **centrifugal mechanisms** such **slider claw** and **revolute claw** and tested their working in **Gazebo**.

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
5. Problems when more than 2 joints (revolute or slider) in a beyblade
6. Contact-related issues (between components in a mechanism like F:D, between 2 beys)
7. Mechanisms like F:D and F:S don't seem to work due to the presence of kinematics loops
8. Manual altering of joint origins ?

Many of these issues can be traced to either one of the 2 - **physics** or **simulator**

Simulator settings might have to be adjusted properly (factors such as friction, collision, etc).

Physics aspects such as moments of inertia have to be considered as well.

Broad classification of problems - **friction, contact, inertias**

**Update on Problem 5**

When CAD Models are converted to urdf format using fusion2urdf, the moments of inertia are on the order of 1e-6, which apparently is too small leading to weird results. On changing the values of the moments of inertia of the base_link to something on the order of 1e-2, the issue is mostly resolved and models with more than 2 prismatic/revolute joints also work.

However, contact and friction related issues still persist. Also, the moments of inertia need to be considered carefully beforehand.

**Insight on residual bouncing**

When the value of **(Given moment of inertia)/(Moment of inertia assuming uniform mass distribution)** is low then the object does not "bounce" when it collides with the ground. Otherwise, it tends to show residual bouncing behaviour (even when coeff of restitution is 0).

So residual bouncing behaviour can be reduced by reducing the given moment of inertia, but this contradicts with the hack in the Problem 5 update. Thus, there exists a tradeoff for now.

**About F:D and F:S**

F:D and F:S involve kinematic loops between the tip, base_link and wing_1 or wing_2 which leads to issues. If the joint between wing_1/wing_2 and tip is removed and the mechanism is allowed to work based on just contact, it barely works but contact related issues arise.

On implementing the splitting method to create kinematic loops, the tip only works when the **selfCollide** tag of every part is set to zero (even then after some time, the rotation of the tip becomes unstable and the tip breaks apart)
