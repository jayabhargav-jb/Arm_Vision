import img_proc
import arm_kinematics
import mapping
import arduino_serial

def main():
    component_2D_coordinates = img_proc.proc_func(1)
    joint_angles_in_deg = arm_kinematics.inverse_kinematics(component_2D_coordinates)
    base_angle = joint_angles_in_deg[0]
    btm_angle = mapping.map_btm(joint_angles_in_deg[1])
    mid_angle = mapping.map_mid(joint_angles_in_deg[2])
    top_angle = mapping.map_top(joint_angles_in_deg[3])
    arduino_serial.pos(base_angle, btm_angle, mid_angle, top_angle)
    arduino_serial.pick()
    arduino_serial.drop()
    return None

if __name__ == "__main__":
    main()