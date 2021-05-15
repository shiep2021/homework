import mySerial as se
import numpy as np
from cv2 import cv2

# Create a image
img=np.zeros((600,600,3), np.uint8)
img[:]=[200,188,188]
k = cv2.waitKey(0)

# 画出方格
cv2.rectangle(img,(100,100),(500,300),(128,0,128),3)
cv2.rectangle(img,(100,300),(500,500),(128,0,128),3)
cv2.rectangle(img,(100,100),(300,500),(128,0,128),3)

# 串口连接
com= se.comPorts(0)
a=se.MXSerial(com,9600)

# 鼠标响应事件
def f_event(event,x,y,flag,param):
    if flag == 1:
        if  x <= 300 and x >= 100 and y <= 300 and y>= 100:
            a.send("1a")
        elif x > 300 and x <= 500 and y <= 300 and y>= 100:
            a.send("2a")
        elif x <= 300 and x >= 100 and y <= 500 and y> 300:
            a.send("3a")
        elif x > 300 and x <= 500 and y <= 500 and y> 300:
            a.send("4a")
        else:
            print ("当前正处于目标圈外")
    elif flag == 2:
        if  x <= 300 and x >= 100 and y <= 300 and y>= 100:
            a.send("1a")
        elif x > 300 and x <= 500 and y <= 300 and y>= 100:
            a.send("2a")
        elif x <= 300 and x >= 100 and y <= 500 and y> 300:
            a.send("3a")
        elif x > 300 and x <= 500 and y <= 500 and y> 300:
            a.send("4a")
        else:
            print ("当前正处于目标圈外")

cv2.namedWindow("example")
cv2.setMouseCallback("example",f_event)

while True:
    cv2.imshow("example", img)
    cv2.waitKey(10) 
