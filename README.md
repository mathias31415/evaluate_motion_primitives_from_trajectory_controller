evaluate_motion_primitives_from_trajectory_controller
==========================================

Package to evaluate trajectory that is approximated using motion primitives

![Licence](https://img.shields.io/badge/License-Apache-2.0-blue.svg)


# Usage notes
Save data (start script before clicking execute in RViz and end script by pressing enter after execution is done):
```
ros2 run evaluate_motion_primitives_from_trajectory_controller record_moprim_from_traj_data
```
Compare data:
```
ros2 run evaluate_motion_primitives_from_trajectory_controller compare
```
or:
```
python3 src/evaluate_motion_primitives_from_trajectory_controller/evaluate_motion_primitives_from_trajectory_controller/compare.py
```