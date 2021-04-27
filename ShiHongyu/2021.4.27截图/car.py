import cv2
import sys
import CarMotor
import threading
import numpy as np
import tkinter

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)
    
top = tkinter.Tk()
top.title("电力大学")
car = CarMotor.CarMotor()

def W():
    car.SetSpeed(80, 80)
def A():
    car.SetSpeed(20, 80)
def S():
    car.SetSpeed(-80, -80)
def D():
    car.SetSpeed(80, 20)
def Stop():
    car.SetSpeed(0, 0)
btn = tkinter.Button(top,text="向前",command=W)
btn.place(x=80,y=50)
btn = tkinter.Button(top,text="向左",command=A)
btn.place(x=10,y=100)
btn = tkinter.Button(top,text="向右",command=D)
btn.place(x=150,y=100)
btn = tkinter.Button(top,text="向后",command=S)
btn.place(x=80,y=150)
btn = tkinter.Button(top,text="Stop",command=Stop)
btn.place(x=80,y=100)
tkinter.Label(top,text= '小车模拟控制器',font=('Arial',14)).place(x=30,y=20)
top.mainloop()
