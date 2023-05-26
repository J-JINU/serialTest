import sys
import serial
import serial.threaded
import serial.tools.list_ports as sp
import time
import datetime as dt
import threading
import signal
import multitimer
import numpy as np
    
serialCom = serial.Serial(port="COM6", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)


def sendData():
    send_cmd = [0x02, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x03]
    serialCom.write(send_cmd)
    print(dt.datetime.now() ,"send cmd : ", send_cmd)
    
arr = np.array([])

def readThread(ser):
    while True:
        if ser.inWaiting() >= 630:
            
            for i in range(30):
                temp = ser.read(21)
                # print(list(array('i', temp)))
                # print(type(np.frombuffer(temp, dtype=np.int8)))
                print(np.frombuffer(temp, dtype=np.uint8))
                # arr = np.append(arr, np.frombuffer(temp, dtype=np.int8), axis=0)
            print("read done", dt.datetime.now())
            print(type(arr))
            return

repeatThread = multitimer.MultiTimer(0.2, sendData)
thread = threading.Thread(target=readThread, args=(serialCom,))

if __name__ == "__main__":
    print("start Serial")
    
    repeatThread.start()
    repeatThread.stop()
    thread.start()

    print("stop Serial")

    # repeatThread.stop()
    # while True: