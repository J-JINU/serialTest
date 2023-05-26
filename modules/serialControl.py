import sys
import serial
import serial.threaded
import serial.tools.list_ports as sp
import time
import threading
import signal


line = []

class serialContorl():
    


def serialOpen():

# with serial.Serial() as serialCom:
#     serialCom.port = "COM6"
#     serialCom.baudrate = 115200
#     serialCom


list = sp.comports()
for port in list:
    print(port)