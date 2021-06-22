#coding=utf-8
import socket
import time
import threading
from numpy import copy
import pygame
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# 颜色
WHITE = (255,255,255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 128)
BLACK = ( 0, 0, 0)

# 创建连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('192.168.136.31',9000))

print('Waiting for connection...')

pygame.init()

# 设置标题
pygame.display.set_caption('UDP 视频传输')

# 开启窗口
display_width = 560
display_height = 320
gameDisplay = pygame.display.set_mode((display_width,display_height))

# 判断是否结束pygame
gamefinish = False
# 帧率
frame_rate = 0

# 通过字体文件获得字体对象
fontObj = pygame.font.Font('‪C:\Windows\Fonts\cambria.ttc'[1:], 20)
# 配置要显示的文字
textSurfaceObj = fontObj.render('FPS', True, BLACK, WHITE)
# 获得要显示的对象的rect
textRectObj = textSurfaceObj.get_rect()
# 设置显示对象的坐标
textRectObj.center = (400, 20)

# 用于视频显示delay
clock = pygame.time.Clock()
# 用于帧率计算
start = time.perf_counter()

while not gamefinish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamefinish = True
            print(event)

    # 无数据接收则线程挂起，等待数据
    data, addr = s.recvfrom(60000)
    frame_rate = frame_rate + 1
    if time.perf_counter() - start > 1:
        start = time.perf_counter()
        # 配置要显示的文字
        textSurfaceObj = fontObj.render(("FPS:" + str(frame_rate)), True, BLACK, WHITE)
        frame_rate = 0


    #print('Received from %s:%s.' % addr)

    # 字符串再转化为图片
    img = pygame.image.frombuffer(data, (160,120), "RGB")

    
    # 直接放大两倍
    img = pygame.transform.scale2x(img)

    # 窗口内设置白色底色和图片，并更新显示
    gameDisplay.fill(WHITE)
    gameDisplay.blit(img, (0, 0))
    gameDisplay.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    clock.tick(60)
    
  
pygame.quit()



