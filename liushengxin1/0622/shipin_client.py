#coding:utf-8
import pygame
import cv2 as cv
#from picamera import PiCamera
import time
import threading
import socket


pygame.init()

# 传输视频信号的UDP 连接进程
def mythread(sock, data, addr):
        sock.sendto(data, addr)
        print("已发送 " + str(len(data)) + " bytes")
        sock.close()

def main():
        print("begin")
        #start = time.clock()
        capture = cv.VideoCapture(0)
        while True:
                ret, frame = capture.read()
                frame = cv.flip(frame, -1)
                frame = cv.resize(frame, (160, 120))
                
                cv.imwrite("test.jpg", frame)
                # 加载图片
                Img = pygame.image.load('test.jpg')
                # 图片转化字符串
                string = pygame.image.tostring(Img, "RGB")
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                t = threading.Thread(target=mythread, args=(sock, string, ('192.168.1.105', 9999)))
                #t.start()
                if cv.waitKey(10) & 0xff == ord('q'):
                        break

main()
cv.destroyAllWindows()
