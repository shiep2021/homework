import numpy as np
import cv2
import mySerial as se

img=np.zeros((512,512,3), np.uint8)
img[:]=[200,5,100]

#串口连接
com= se.comPorts(0)
a=se.MXSerial(com,9600)

cv2.line(img,(100,100),(400,100),(255,255,255),5) 
cv2.line(img,(100,250),(400,250),(255,255,255),5)
cv2.line(img,(100,400),(400,400),(255,255,255),5)

cv2.line(img,(100,100),(100,400),(255,255,255),5)
cv2.line(img,(250,100),(250,400),(255,255,255),5)
cv2.line(img,(400,100),(400,400),(255,255,255),5)


def f_event(event,x,y,flag,param):
        print (event,x,y,flag,param)
        if x>=100 and x<=250 and y>=100 and y<=250:
            print ("第一格")
        if event == 1 and flag ==1 :
            a.send("1a")


        if x>=250 and x<=400 and y>=100 and y<=250:
            print ("第二格")
        if event == 1 and flag ==1 :
            a.send("2a")



        if x>=100 and x<=250 and y>=250 and y<=400:
            print ("第三格")
        if event == 1 and flag ==1 :
            a.send("3a")
 


        if x>=250 and x<=400 and y>=250 and y<=400:
            print ("第四格")
        if event == 1 and flag ==1 :
            a.send("4a")



cv2.namedWindow("SiuGongGe")
cv2.setMouseCallback("SiuGongGe",f_event)
while True:
    cv2.waitKey(10)
    cv2.imshow("SiuGongGe",img)