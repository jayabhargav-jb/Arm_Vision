"""
Serial Communiation Link for the Arduino

Connect to /dev/ttyACM0 and send commands to the Arduino

Commands:
    home(): Home the robot
    pos(bas, btm, mid, top): Move the robot to position
    pick(): Turn on the electromagnet
    drop(): Drop the object at drop position
    rest(): Rest the robot, for least torque on the motors
"""

import serial
from time import sleep

s = serial.Serial("/dev/ttyACM0")

s.write("home".encode())
sleep(2)
def wait():
    """Wait for Arduino to complete the serial print"""
    line = str("")
    while line.find("Ready for Input") != -1:
        line = s.readline()
#        if line != "":
#            print(line)

def pos(bas, btm, mid, top):
    """Move arm to positions given in the arguments"""
    s.write(("bas, "+ str(bas)).encode())
    print("Moved base")
    sleep(2)
    s.write(("btm, "+ str(btm)).encode())
    print("Moved bottom")
    sleep(2)
    s.write(("mid, "+ str(mid)).encode())
    print("Moved mid")
    sleep(2)
    s.write(("top, "+ str(top)).encode())
    print("Moved top")
    sleep(2)

def drop():
    """Drop the picked item"""
    s.write(b"drop")
    sleep(2)

def pick():
    """Turn on the electro-magnet"""
    s.write(b"pick")
    sleep(2)

def home():
    """Home the robot"""
    s.write(b"home")
    sleep(2)

def rest():
    """Robot position for rest"""
    s.write(b"rest")
    sleep(2)

