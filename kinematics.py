# import visual_kinematics as vk
from roboticstoolbox import *
import numpy as np

l1_d = (4.5-0.15)*2/5
l2_a = 0.6
l2_alp = np.pi/2
l3_a = 12.2-0.15
l4_a = 5.8-0.15
l5_a = 4.5-0.15

# L1[1] = Link('revolute', 'd', l1_d, 'a', 0, 'alpha', 0, 'modified')
# L1[2] = Link('revolute', 'd', 0, 'a', l2_a, 'alpha', l2_alp, 'modified')
# L1[3] = Link('revolute', 'd', 0, 'a', l3_a, 'alpha', 0, 'modified')
# L1[4] = Link('revolute', 'd', 0, 'a', l4_a, 'alpha', 0, 'modified')
# L1[5] = Link('revolute', 'd', 0, 'a', l5_a, 'alpha', 0, 'modified')

dh_params = np.array([])
