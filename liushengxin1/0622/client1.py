import socket
HOST = '192.168.136.61'
PORT =21567
BUFSIZE=1024
ADDR =(HOST,PORT)

import tkinter
import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
top=tkinter.Tk() 
import cv2
import cv2 as cv
import threading
import time

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(ADDR)
while True:
    data=''
    top.title("电力大学")
    def F():
        print("向前，已经被点击")
        words="向前"
        speaker.Speak(words)
        data='xiangqian'
        s.send(bytes(data,'utf-8'))
    def B():
        print("向后，已经被点击")
        words="向后"
        speaker.Speak(words)
        data='xianghou'
        s.send(bytes(data,'utf-8'))
    def Na():
        print("向左，已经被点击")
        words="向左"
        speaker.Speak(words)
        data='xiangzuo'
        s.send(bytes(data,'utf-8'))
    def you():
        print("向右，已经被点击")
        words="向右"
        speaker.Speak(words)
        data='xiangyou'
        s.send(bytes(data,'utf-8'))
    def S():
        print("停止，已经被点击")
        words="停止"
        speaker.Speak(words)
        data='tingzhi'
        s.send(bytes(data,'utf-8'))
    btn=tkinter.Button(top,text="向前",command=F)

    btn.place(x=100,y=40)

    btn=tkinter.Button(top,text="向左",command=Na)


    btn.place(x=60,y=70)

    btn=tkinter.Button(top,text="向右",command=you)

    btn.place(x=140,y=70)
    btn=tkinter.Button(top,text="向后",command=B)

    btn.place(x=100,y=100)

    btn=tkinter.Button(top,text="停止",command=S)

    btn.place(x=100,y=70)
    tkinter.Label(top,text='小车模拟器',font=('Arial',10)).place(x=50,y=10)
    top.mainloop()

 

s.close()
