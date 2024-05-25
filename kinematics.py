# import visual_kinematics as vk
from roboticstoolbox import *
from spatialmath import SE3
import numpy as np






# l1_d = 4.1
l1_d = 2.6
l1_a = 0.8
l2_a = 12.7
l3_a = 7.7 
l4_a = 5.4

# | Cur |   0 | 130 |  90 |  10 |
#         -23   -18    13     0

L1 = list()

# L1.append(RevoluteDH(d=l1_d, a=l2_a, alpha=np.pi/2, qlim=np.array([-58,-28 ]))) # min=0, max=100    
# L1.append(RevoluteDH(d=0, a= l3_a, alpha=0, qlim=np.array([-60,-8 ]))) # min=170, max = 20 INVERSE MAPPED
# L1.append(RevoluteDH(d=0, a= l4_a, alpha=0, qlim=np.array([ 15,69])))# min = 90-21 = 69, max = 90-75 = 15
# L1.append(RevoluteDH(d=0, a= l5_a, alpha=0, qlim=np.array([ 90,0])))# min = 10, max= 95

L1.append(RevoluteDH(d=l1_d, a=l1_a, alpha=np.pi/2))
L1.append(RevoluteDH(d=0, a= l2_a, alpha=0))
L1.append(RevoluteDH(d=0, a= l3_a, alpha=0))
L1.append(RevoluteDH(d=0, a= l4_a, alpha=0))
arm = SerialLink(L1)




# Z offset 2.4 cm
angles = [0, 13 *np.pi/180, -18 *np.pi/180, -23 *np.pi/180]

print(angles)
hom_mat = arm.fkine(angles)
# print(type(hom_mat))
print("fkine matrix:\n", hom_mat)
z = 2.25
x = 25.613
y = 0
req_position_arr = [x, y, z]
req_pose_arr = [[0.8829, 0.4695, 0, x], [0, 0, -1, y], [-0.4695, 0.8829, 0, z], [0,0,0,1]]
print(req_pose_arr)
se3_obj = SE3(req_pose_arr)
req_pose_se3 = SE3(req_pose_arr)

# print(arm.ikine_LM(hom_mat).q)


joint_angles = arm.ikine_LM(req_pose_se3).q
print(joint_angles[0]*(180/np.pi), joint_angles[1]*(180/np.pi), joint_angles[2]*(180/np.pi), joint_angles[3]*(180/np.pi))

# print(arm._T)
# arm.teach()