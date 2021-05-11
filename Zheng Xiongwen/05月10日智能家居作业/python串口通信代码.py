import mySerial as se
import cv2
import numpy as np
# 串口连接
com = se.comPorts(0)
a = se.MXSerial(com, 9600)

msg = -1

def draw_circle(event,x,y,flags,param):
    global msg
    # print(event,x,y)
    if event == 1 :
        if x<300 and y<300:
            a.send("1a")
        elif x>300 and y<300:
            a.send("2a")
        elif x<300 and  y>300:
            a.send("3a")
        elif x > 300 and y > 300:
            a.send("4a")
        else:
            pass
    else:
        pass
    # if event==cv2.EVENT_LBUTTONDBLCLK:
    #     cv2.circle(img,(x,y),100,(255,0,0),-1)

# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((600, 600, 3), np.uint8)
img[:]=[255,255,255]

cv2.line(img, (300, 0), (300, 600), (60, 60, 60), 2)
cv2.line(img, (0, 300), (600, 300), (60, 60, 60), 2)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

try:
    while True:
        cv2.imshow('image',img)
        if cv2.waitKey(20)&0xFF==27:
            break
except KeyboardInterrupt:
    a.close()

cv2.destroy