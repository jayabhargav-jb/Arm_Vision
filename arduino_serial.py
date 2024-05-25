import serial
from time import sleep

s = serial.Serial("/dev/ttyACM0")

s.write("home".encode())

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
    wait()

def pick():
    """Turn on the electro-magnet"""
    s.write(b"pick")
    wait()


