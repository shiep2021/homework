import numpy as np
import cv2
from os import system
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
chess = np.zeros((3,3),np.uint8)
flag = 0
turn = 0
img = np.zeros((512,512,3), np.uint8)


def f_event(event,x,y,flag,param):  #鼠标进行操作时的回调函数
    global chess,turn
    unit = 0
    Px = 0
    Py = 0
    for i in range(1,4):    #判定鼠标所在区域位于哪个格
        for j in range(1,4):
            if j*102 < x < 102+j*102 and i*102 < y < 102+i*102:
                unit = j+3*(i-1)
                Px = j
                Py = i
    if event == cv2.EVENT_LBUTTONDOWN and Px != 0 and Py != 0:  #如果按下鼠标且没有按到棋盘外则执行
        if Px == 0 or Py == 0: return
        if not chess[Py-1,Px-1]:    #如果某个格为空则执行
            chess[Py-1,Px-1]= turn%2 + 1
            DrawChess(Px,Py,turn%2 + 1)
            turn += 1
        WhoWin()

def DrawChess(x,y,team):    #更新棋盘画面
    if team == 1:   #白棋
        cv2.circle(img,(54 + x*102,54 + y * 102),48,(255,255,255),-1)
        cv2.circle(img,(50,450),24,(0,0,0),-1)
    else:   #黑棋
        cv2.circle(img,(54 + x*102,54 + y * 102),48,(0,0,0),-1)
        cv2.circle(img,(50,450),24,(255,255,255),-1)

def WhoWin():   #判断输赢
    global flag

    if (chess>0).all(): #如果棋盘满格，平局
        flag = 3

    for i in range(3):  #连成横或竖的直线
        if chess[i,0] == chess[i,1] == chess[i,2]:
            if chess[i,0] == 1:
                flag = 1
            elif chess[i,0] == 2:
                flag = 2
        if chess[0,i] == chess[1,i] == chess[2,i]:
            if chess[0,i] == 1:
                flag = 1
            elif chess[0,i] == 2:
                flag = 2
    if chess[0,0] == chess[1,1] == chess[2,2] or chess[0,2] == chess[1,1] == chess[2,0]:    #连成斜线
        if chess[1,1] == 1:
                flag = 1
        elif chess[1,1] == 2:
                flag = 2


img[:] = [200,5,100]
for i in range(3):
    for j in range(3):
        cv2.rectangle(img,(102+j*102,102+i*102),(204+j*102,204+i*102),(255,255,255),3)  #绘制棋盘

cv2.circle(img,(50,450),24,(255,255,255),-1)
cv2.namedWindow('ABC')
cv2.setMouseCallback("ABC",f_event)

while True:
    cv2.waitKey(100)
    cv2.imshow("ABC",img)
    if flag: break

if flag == 1:   #游戏结束
    print("白旗胜利")
    speaker.Speak("白旗胜利")
elif flag == 2:
    print("黑旗胜利")
    speaker.Speak("黑旗胜利")
else:
    print("平局")
    speaker.Speak("平局")
    
