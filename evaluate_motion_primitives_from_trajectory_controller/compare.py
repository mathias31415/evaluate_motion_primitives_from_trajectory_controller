#!/usr/bin/env python3

# Copyright (c) 2025, Mathias Fuhrer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Mathias Fuhrer

import os
import pandas as pd

# to run with ros2 run ...
# from evaluate_motion_primitives_from_trajectory_controller.compare_planned_and_executed_trajectory import (
#     compare_and_plot_joint_trajectories,
#     compare_and_plot_cartesian_trajectories,
# )
# from evaluate_motion_primitives_from_trajectory_controller.compare_planned_and_reduced_points import (
#     plot_cartesian_trajectory,
#     plot_joint_trajectory,
# )
# from evaluate_motion_primitives_from_trajectory_controller.fk_client import FKClient

# to run with python3
from compare_planned_and_executed_trajectory import (
    compare_and_plot_joint_trajectories,
    compare_and_plot_cartesian_trajectories,
)
from compare_planned_and_reduced_points import plot_cartesian_trajectory, plot_joint_trajectory
from fk_client import FKClient


def main():
    data_dir = "src/evaluate_motion_primitives_from_trajectory_controller/data"
    ### UR ###
    # filename_planned = "trajectory_20250715_114409_planned.csv"
    # filename_executed = "trajectory_20250715_114409_executed.csv"
    # filename_reduced = "trajectory_20250715_114409_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250715_114057_planned.csv"
    # filename_executed = "trajectory_20250715_114057_executed.csv"
    # filename_reduced = "trajectory_20250715_114057_reduced_LIN.csv"
    # mode = "cartesian"

    filename_planned = "trajectory_20250716_090701_planned.csv"
    filename_executed = "trajectory_20250716_090701_executed.csv"
    filename_reduced = "trajectory_20250716_090701_reduced_LIN.csv"
    mode = "cartesian"

    # filename_planned = "trajectory_20250716_091324_planned.csv"
    # filename_executed = "trajectory_20250716_091324_executed.csv"
    # filename_reduced = "trajectory_20250716_091324_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250716_092410_planned.csv"
    # filename_executed = "trajectory_20250716_092410_executed.csv"
    # filename_reduced = "trajectory_20250716_092410_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250716_093119_planned.csv"
    # filename_executed = "trajectory_20250716_093119_executed.csv"
    # filename_reduced = "trajectory_20250716_093119_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250716_093707_planned.csv"
    # filename_executed = "trajectory_20250716_093707_executed.csv"
    # filename_reduced = "trajectory_20250716_093707_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250716_101518_planned.csv"
    # filename_executed = "trajectory_20250716_101518_executed.csv"
    # filename_reduced = "trajectory_20250716_101518_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250716_101907_planned.csv"
    # filename_executed = "trajectory_20250716_101907_executed.csv"
    # filename_reduced = "trajectory_20250716_101907_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250721_152220_planned.csv"
    # filename_executed = "trajectory_20250721_152220_executed.csv"
    # filename_reduced = "trajectory_20250721_152220_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250722_124049_planned.csv"
    # filename_executed = "trajectory_20250722_124049_executed.csv"
    # filename_reduced = "trajectory_20250722_124049_reduced_LIN.csv"
    # mode = "cartesian"

    ### KUKA ###
    # filename_planned = "trajectory_20250722_094638_planned.csv"
    # filename_executed = "trajectory_20250722_094638_executed.csv"
    # filename_reduced = "trajectory_20250722_094638_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250722_095053_planned.csv"
    # filename_executed = "trajectory_20250722_095053_executed.csv"
    # filename_reduced = "trajectory_20250722_095053_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250722_095544_planned.csv"
    # filename_executed = "trajectory_20250722_095544_executed.csv"
    # filename_reduced = "trajectory_20250722_095544_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250722_095840_planned.csv"
    # filename_executed = "trajectory_20250722_095840_executed.csv"
    # filename_reduced = "trajectory_20250722_095840_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250722_100251_planned.csv"
    # filename_executed = "trajectory_20250722_100251_executed.csv"
    # filename_reduced = "trajectory_20250722_100251_reduced_PTP.csv"
    # mode = "joint"

    # filename_planned = "trajectory_20250722_100934_planned.csv"
    # filename_executed = "trajectory_20250722_100934_executed.csv"
    # filename_reduced = "trajectory_20250722_100934_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250722_101230_planned.csv"
    # filename_executed = "trajectory_20250722_101230_executed.csv"
    # filename_reduced = "trajectory_20250722_101230_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250722_101641_planned.csv"
    # filename_executed = "trajectory_20250722_101641_executed.csv"
    # filename_reduced = "trajectory_20250722_101641_reduced_LIN.csv"
    # mode = "cartesian"
    
    # filename_planned = "trajectory_20250722_102250_planned.csv"
    # filename_executed = "trajectory_20250722_102250_executed.csv"
    # filename_reduced = "trajectory_20250722_102250_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250722_103002_planned.csv"
    # filename_executed = "trajectory_20250722_103002_executed.csv"
    # filename_reduced = "trajectory_20250722_103002_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250722_103755_planned.csv"
    # filename_executed = "trajectory_20250722_103755_executed.csv"
    # filename_reduced = "trajectory_20250722_103755_reduced_LIN.csv"
    # mode = "cartesian"

    # filename_planned = "trajectory_20250722_104157_planned.csv"
    # filename_executed = "trajectory_20250722_104157_executed.csv"
    # filename_reduced = "trajectory_20250722_104157_reduced_LIN.csv"
    # mode = "cartesian"

    filepath_planned = os.path.join(data_dir, filename_planned)
    filepath_executed = os.path.join(data_dir, filename_executed)
    filepath_reduced = os.path.join(data_dir, filename_reduced)

    ## UR ###
    joint_names = [
        "shoulder_pan_joint",
        "shoulder_lift_joint",
        "elbow_joint",
        "wrist_1_joint",
        "wrist_2_joint",
        "wrist_3_joint",
    ]
    joint_pos_names = [
        "shoulder_pan_joint_pos",
        "shoulder_lift_joint_pos",
        "elbow_joint_pos",
        "wrist_1_joint_pos",
        "wrist_2_joint_pos",
        "wrist_3_joint_pos",
    ]
    joint_vel_threshold = 0.01

    ### KUKA ###
    # joint_names = [
    #     "joint_a1",
    #     "joint_a2",
    #     "joint_a3",
    #     "joint_a4",
    #     "joint_a5",
    #     "joint_a6",
    # ]
    # joint_pos_names = [
    #     "joint_a1_pos",
    #     "joint_a2_pos",
    #     "joint_a3_pos",
    #     "joint_a4_pos",
    #     "joint_a5_pos",
    #     "joint_a6_pos",
    # ]
    # joint_vel_threshold = 1.0

    pose_names = ["pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw"]

    # Load the executed CSV
    df_executed = pd.read_csv(filepath_executed)

    # Check if the pose_names columns are present
    if not all(col in df_executed.columns for col in pose_names):
        print("Pose columns are missing in the executed file, computing them with FK...")

        fk = FKClient()

        # List to store the computed poses
        poses = []

        # Iterate over each row
        for idx, row in df_executed.iterrows():
            joint_positions = [row[joint_pos] for joint_pos in joint_pos_names]
            pose = fk.compute_fk(joint_names, joint_positions)
            if pose is None:
                # If FK fails, e.g. None, fill with NaN
                poses.append([float("nan")] * 7)
            else:
                # Extract pose as list [x, y, z, qx, qy, qz, qw]
                poses.append(
                    [
                        pose.position.x,
                        pose.position.y,
                        pose.position.z,
                        pose.orientation.x,
                        pose.orientation.y,
                        pose.orientation.z,
                        pose.orientation.w,
                    ]
                )

        fk.shutdown()

        # Add the computed poses as new columns
        for i, col in enumerate(pose_names):
            df_executed[col] = [pose[i] for pose in poses]

        # Save the CSV with the new columns
        df_executed.to_csv(filepath_executed, index=False)
        print(f"Pose columns added to {filepath_executed} and saved.")

    else:
        print("Pose columns are already present in the executed file.")

    # compare planned and reduced trajectory
    if mode == "cartesian":
        plot_cartesian_trajectory(filepath_planned, filepath_reduced, pose_names)
    elif mode == "joint":
        plot_joint_trajectory(filepath_planned, filepath_reduced, joint_pos_names)

    # compare planned and executed trajectory
    compare_and_plot_joint_trajectories(
        filepath_planned, filepath_executed, joint_pos_names, n_points=100, vel_threshold=joint_vel_threshold
    )
    compare_and_plot_cartesian_trajectories(
        filepath_planned, filepath_executed, pose_names, n_points=100, vel_threshold=joint_vel_threshold
    )


if __name__ == "__main__":
    main()
