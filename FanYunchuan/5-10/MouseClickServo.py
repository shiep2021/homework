import cv2
import numpy as np
import mySerial as se

#串口连接
com= se.comPorts(0)
a=se.MXSerial(com,9600)


#鼠标事件定义
def draw_circle(event,x,y,flags,param):
    print(event)
    if event == 1 :
        if x<256 and y<256:
            a.send("1a")
        elif x>256 and y<256:
            a.send("2a")
        elif x<256 and  y>256:
            a.send("3a")
        elif x>256 and y>256:
            a.send("4a")
        else:
            pass
    else:
        pass

# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
img[:]=[255,255,255]
cv2.line(img, (256, 0), (256, 512), (60, 60, 60), 2)
cv2.line(img, (0, 256), (512, 256), (60, 60, 60), 2)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)


try:
    while True:
        cv2.imshow('image',img)
        if cv2.waitKey(20)&0xFF==27:
            break
    cv2.destroy
except KeyboardInterrupt:
    a.close()


