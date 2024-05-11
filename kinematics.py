# import visual_kinematics as vk
from roboticstoolbox import *
import numpy as np

l1_d = 4.3
l2_a = 0.6
l2_alp = np.pi/2
l3_a = 13.1
l4_a = 5.4
l5_a = 4.8

L1 = list()

L1.append(RevoluteDH(d=l1_d, a=l2_a, alpha=np.pi/2, qlim = [-28, -58])) # min=0, max=100    
L1.append(RevoluteDH(d=0, a= l3_a, alpha=0, qlim=[-8, -60])) # min=170, max = 20 INVERSE MAPPED
L1.append(RevoluteDH(d=0, a= l4_a, alpha=0, qlim=[69, 15]))# min = 90-21 = 69, max = 90-75 = 15
L1.append(RevoluteDH(d=0, a= l5_a, alpha=0, qlim=[0, 90]))# min = 10, max= 95



# L1[1] = Link('revolute', 'd', l1_d, 'a', 0, 'alpha', 0, 'modified')
# L1[2] = Link('revolute', 'd', 0, 'a', l2_a, 'alpha', l2_alp, 'modified')
# L1[3] = Link('revolute', 'd', 0, 'a', l3_a, 'alpha', 0, 'modified')
# L1[4] = Link('revolute', 'd', 0, 'a', l4_a, 'alpha', 0, 'modified')
# L1[5] = Link('revolute', 'd', 0, 'a', l5_a, 'alpha', 0, 'modified')
arm = SerialLink(L1)

hom_mat = arm.fkine([0, 0, 0, 0])

print(arm.ikine_LM(hom_mat))
print(arm._T)
# arm.teach()