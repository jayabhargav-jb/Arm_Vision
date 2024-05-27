from fastapi import FastAPI
from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# import img_proc
# import arm_kinematics
import mapping
# import arduino_serial

app = FastAPI()

# To serve static files from static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/res")
async def pick_res():
    # component_2D_coordinates = img_proc.proc_func(user_input="RESISTOR")
    # joint_angles_in_deg = arm_kinematics.inverse_kinematics(component_2D_coordinates)
    # base_angle = joint_angles_in_deg[0]
    # btm_angle = mapping.map_btm(joint_angles_in_deg[1])
    # mid_angle = mapping.map_mid(joint_angles_in_deg[2])
    # top_angle = mapping.map_top(joint_angles_in_deg[3])
    # arduinostatic_serial.pos(base_angle, btm_angle, mid_angle, top_angle)
    # arduino_serial.pick()
    # arduino_serial.drop()
    print("RES")

@app.get("/cap")
async def pick_res():
    # component_2D_coordinates = img_proc.proc_func(user_input="CAPACITOR")
    # joint_angles_in_deg = arm_kinematics.inverse_kinematics(component_2D_coordinates)
    # base_angle = joint_angles_in_deg[0]
    # btm_angle = mapping.map_btm(joint_angles_in_deg[1])
    # mid_angle = mapping.map_mid(joint_angles_in_deg[2])
    # top_angle = mapping.map_top(joint_angles_in_deg[3])
    # arduinostatic_serial.pos(base_angle, btm_angle, mid_angle, top_angle)
    # arduino_serial.pick()
    # arduino_serial.drop()
    print("CAP")
