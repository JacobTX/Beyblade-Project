# Technical details

## Simulation aspects 

Currently the Beyblade is modelled as a cone.

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

### Physics parameters

[Link](https://classic.gazebosim.org/tutorials?tut=physics_params&cat=physics)

### Convert CAD model in Fusion360 to URDF

[How to install Fusion2URDF Plugin || Use Autodesk Fusion 360 designs in ROS Simulation as URDF](https://www.youtube.com/watch?v=TitHYg-5_j8&t=244s&ab_channel=PranshuTople)

## Mechanism design aspects

1) Links
2) Gears
3) DOF
4) Springs
5) Dampers
6) Magnets 
7) Hydraulics
