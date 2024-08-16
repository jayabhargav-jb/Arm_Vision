# import visual_kinematics as vk
from roboticstoolbox import *
from spatialmath import SE3
import numpy as np
import img_proc


def inverse_kinematics(xy_tuple):
    l1_d = 2.6
    l1_a = 0.8
    l2_a = 12.7
    l3_a = 7.7 
    l4_a = 5.4

    # | Cur |   0 | 130 |  90 |  10 |
    #         -23   -18    13     0

    L1 = list()

    L1.append(RevoluteDH(d=l1_d, a=l1_a, alpha=np.pi/2, qlim=np.array([0 * (np.pi/180), 90 * (np.pi/180)]))) # min=0, max=100    
    L1.append(RevoluteDH(d=0, a= l2_a, alpha=0, qlim=np.array([11 * (np.pi/180), 68 * (np.pi/180)]))) # min=170, max = 20 INVERSE MAPPED
    L1.append(RevoluteDH(d=0, a= l3_a, alpha=0, qlim=np.array([-57 * (np.pi/180), -8 * (np.pi/180)])))# min = 90-21 = 69, max = 90-75 = 15
    L1.append(RevoluteDH(d=0, a= l4_a, alpha=0, qlim=np.array([-70 * (np.pi/180), -27 * (np.pi/180)])))# min = 10, max= 95

    arm = SerialLink(L1)

    # x, y = img_proc.proc_func(1)
    x, y = xy_tuple
    z = 1.2
    joint_angles = [0, 0, 0, 0]
    # req_position_arr = [x, y, z]
    req_pose_arr = [[0.8829, 0.4695, 0, x], [0, 0, -1, y], [-0.4695, 0.8829, 0, z], [0,0,0,1]]
    # req_pose_arr = [[1,0,0, x], [0, 1, 0, y], [0,0,1, z], [0,0,0,1]]
    req_pose_se3 = SE3(req_pose_arr)
    # print(x,y,z)
    # while joint_angles[1]<30:
    joint_angles = arm.ikine_LM(req_pose_se3).q

    # print(joint_angles[0]*(180/np.pi), joint_angles[1]*(180/np.pi), joint_angles[2]*(180/np.pi), joint_angles[3]*(180/np.pi))

    return joint_angles[0]*(180/np.pi), joint_angles[1]*(180/np.pi), joint_angles[2]*(180/np.pi), joint_angles[3]*(180/np.pi)
