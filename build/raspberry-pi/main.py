from fastapi import FastAPI
from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from time import sleep
import img_proc
import arm_kinematics
import mapping
import arduino_serial

app = FastAPI()

# To serve static files from static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/res")
async def pick_res():
    component_2D_coordinates = img_proc.proc_func(1, user_input="RESISTOR")
    joint_angles_in_deg = arm_kinematics.inverse_kinematics(component_2D_coordinates)
    base_angle = joint_angles_in_deg[0]
    btm_angle = mapping.map_btm(joint_angles_in_deg[1])
    mid_angle = mapping.map_mid(joint_angles_in_deg[2])
    top_angle = mapping.map_top(joint_angles_in_deg[3])
    arduino_serial.pos(base_anle, btm_anle, mid_anle, top_anle)
    sleep(3)
    arduino_serial.pick()
    sleep(2)
    arduino_serial.drop()
    print("RES")

@app.get("/cap")
async def pick_cap():
    component_2D_coordinates = img_proc.proc_func(user_input="CAPACITOR")
    joint_angles_in_deg = arm_kinematics.inverse_kinematics(component_2D_coordinates)
    base_angle = joint_angles_in_deg[0]
    btm_angle = mapping.map_btm(joint_angles_in_deg[1])
    mid_angle = mapping.map_mid(joint_angles_in_deg[2])
    top_angle = mapping.map_top(joint_angles_in_deg[3])
    arduino_serial.pos(base_angle, btm_angle, mid_angle, top_angle)
    arduino_serial.pick()
    arduino_serial.drop()
    print("CAP")

"""    
    component_2D_coordinates = img_proc.proc_func(1, user_input="RESISTOR")
    # x,z = component_2D_coordinates
    joint_angles_in_deg = arm_kinematics.inverse_kinematics(component_2D_coordinates)
    print("joint angles:", joint_angles_in_deg)
    base_angle = joint_angles_in_deg[0]
    btm_angle = mapping.map_btm(joint_angles_in_deg[1])
    mid_angle = mapping.map_mid(joint_angles_in_deg[2])
    top_angle = mapping.map_top(joint_angles_in_deg[3])
    print("arduino angles",int(base_angle), int(btm_angle), int(mid_angle), int(top_angle))
    arduino_serial.pos(int(base_angle), int(btm_angle), int(mid_angle), int(top_angle))
    arduino_serial.pick()
    arduino_serial.drop()
    return None
"""

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

















































base_anle = 45
btm_anle = 50
mid_anle = 45
top_anle = 30
