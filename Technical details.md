# Technical details

## Simulation aspects 

### Applying force/torque on a link

Let the model be **Top3** and the link be **link_0**

Apply **force**

```

rosservice call /gazebo/apply_body_wrench '{body_name: "Top3::link_0" , wrench: { force: { x: 0, y: 10 , z: 0 } }, start_time: 10000000000, duration: 1000000000 }'
```

Apply **torque**

```
 rosservice call /gazebo/apply_body_wrench '{body_name: "Top3::link_0" , wrench: { torque: { x: 0, y: 0 , z: 10 } }, start_time: 10000000000, duration: 1000000000 }
```

[ROS Communication](http://gazebosim.org/tutorials/?tut=ros_comm)

### Spawning a model in Gazebo

[How to spawn an SDF custom model in Gazebo with ROS](https://www.youtube.com/watch?v=2UZFzpd5pKk&ab_channel=TheConstruct)

Spawning **Top3**

```
<node name="spawner" pkg="gazebo_ros" type="spawn_model" args="-file /home/jacob/model_editor_models/Top3/model.sdf -sdf -x 0.0 -y 0.0 -z 1.0 -R 0.1 -model beyblade" />
```

### Rigidly fixing a link to the world

[Link](https://classic.gazebosim.org/tutorials?tut=ros_urdf)

### Model a 4-bar linkage in SDFormat and URDF

[Link](https://classic.gazebosim.org/tutorials?tut=kinematic_loop&cat=)

### Physics parameters

[Link](https://classic.gazebosim.org/tutorials?tut=physics_params&cat=physics)

### Aerodynamics

[Link](https://classic.gazebosim.org/tutorials?tut=aerodynamics&cat=physics)

### Convert CAD model in Fusion360 to URDF

[How to install Fusion2URDF Plugin || Use Autodesk Fusion 360 designs in ROS Simulation as URDF](https://www.youtube.com/watch?v=TitHYg-5_j8&t=244s&ab_channel=PranshuTople)

### SOLIDWORKS to Gazebo

[[ROS Tutorials] How to open a solidworks model in gazebo](https://www.youtube.com/watch?v=T7X_p_KMwus&t=903s&ab_channel=TheConstruct)
## Mechanism design aspects

**Documentation** and **Version Control** are important while designing for large **scale** and **complexity**

**SEACAM**

<ol>
<li>Science
 <ol>
 <li> Solid Mechanics, Structural Materials
 <li> Fluid Mechanics, Thermodynamics, Heat transfer
 <li> Kinematics and Dynamics of Machines 
  <ol>
   <li> Mass, COM, Moments of inertia
   <li> Links, Gears
   <li> Inclined planes (refer F:D and F:S tips), Springs, Dampers
   <li> Magnets / Electromagnetics
   <li> Pneumatics and Hydraulics
   <li> DOF
  </ol>
 <li> Common sense 
  <ol>
   <li> Geometric constraints (size, etc)
   <li>Weight
  </ol>
 </ol>
<li> Ergonomics
<li> Aesthetic
<li> Cost
<li> Assembly - Joining techniques(adhesive, fasteners), Ease, Tolerance, Clearance
<li> Manufacturability 
</ol>
