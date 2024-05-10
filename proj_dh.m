clear
syms q1 q2 q3 q4 q5
% shaft diameter = 0.15, subtracted from length cause measured distance is
% from shaft edge to shaft edge.
l1_d = (4.5-0.15)*2/5;
l2_a = 0.6;
l2_alp = pi/2;
l3_a = 12.2-0.15;
l4_a = 5.8-0.15; 
l5_a = 4.5-0.15; % do not consider rotation.

L1(1) = Link('revolute', 'd', l1_d, 'a', 0, 'alpha', 0, 'modified');
L1(2) = Link('revolute', 'd', 0, 'a', l2_a, 'alpha', l2_alp, 'modified');
L1(3) = Link('revolute', 'd', 0, 'a', l3_a, 'alpha', 0, 'modified');
L1(4) = Link('revolute', 'd', 0, 'a', l4_a, 'alpha', 0, 'modified');
L1(5) = Link('revolute', 'd', 0, 'a', l5_a, 'alpha', 0, 'modified');

arm = SerialLink(L1, 'name', 'arm');
% fkine_mat = vpa(arm.fkine([q1 q2 q3 q4 q5]),3);
fkine_mat = vpa(arm.fkine([30 30 30 30 30]),3);
fkine_mat.T

arm.ikine(fkine_mat.T, )
arm.teach()