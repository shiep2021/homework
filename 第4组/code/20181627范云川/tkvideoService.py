import socket
import cv2
import numpy
import copy
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk#图像控件
import os
def tkImage(frame):
    frame = cv2.flip(frame, 1) #摄像头翻转
    cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    pilImage=Image.fromarray(cvimage)
    pilImage = pilImage.resize((600, 500),Image.ANTIALIAS)
    tkImage =  ImageTk.PhotoImage(image=pilImage)
    return tkImage
def ReceiveVideo():
    #图像保存功能初始化
    times=0
    temp=0
    #提取视频的频率
    frameFrequency=100
    #输出图片到当前目录vedio文件夹下
    outPutDirName='vedio/'
    if not os.path.exists(outPutDirName):
        #如果文件目录不存在则创建目录
        os.makedirs(outPutDirName)

    #tkinter界面初始化
    top = tk.Tk()
    top.title('视频窗口')
    top.geometry('900x600')
    image_width = 600
    image_height = 500
    canvas = Canvas(top,bg = 'white',width = image_width,height = image_height )#绘制画布
    Label(top,text = '中国航天工业集团',font = ("黑体",14),width =15,height = 1).place(x =400,y = 20,anchor = 'nw')
    canvas.place(x = 150,y = 50)


    # IP地址'0.0.0.0'为等待客户端47接
    address = ('192.168.43.47', 2345)
    #address = ('10.56.21.13', 2345)
    
    # 建立socket对象，参数意义见https://blog.csdn.net/rebelqsp/article/details/22109925
    # socket.AF_INET：服务器之间网络通信
    # socket.SOCK_STREAM：流式socket , for TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将套接字绑定到地址, 在AF_INET下,以元组（host,port）的形式表示地址.
    s.bind(address)
    # 开始监听TCP传入连接。参数指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
    s.listen(5)

    def recvall(sock, count):
        buf = b''  # buf是一个byte类型
        while count:
            # 接受TCP套接字的数据。数据以字符串形式返回，count指定要接收的最大数据量.
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    # 接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。addr是连接客户端的地址。
    # 没有连接则等待有连接
    conn, addr = s.accept()
    print('connect from:' + str(addr))
    while 1:
        times+=1# 用于计算帧率信息
        length = recvall(conn, 16)  # 获得图片文件的长度,16代表获取长度
        stringData = recvall(conn, int(length))  # 根据获得的文件长度，获取图片文件
        data = numpy.frombuffer(stringData, numpy.uint8)  # 将获取到的字符流数据转换成1维数组
        decimg = cv2.imdecode(data, cv2.IMREAD_COLOR)  # 将数组解码成图像
        #cv2.imshow('SERVER', decimg)  # 显示图像

        if times%frameFrequency==0:#保存图像
            temp+=1
            cv2.imwrite(outPutDirName + str(temp)+'.jpg', image)


        pic = tkImage(decimg)#将图像数据显示到tkinter上
        canvas.create_image(0,0,anchor = 'nw',image = pic)
        top.update()
 

        # # 将帧率信息回传，主要目的是测试可以双向通信

        image = copy.deepcopy(decimg)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
        result, imgencode = cv2.imencode('.jpg', image, encode_param)
        # 建立矩阵
        data = numpy.array(imgencode)
        # 将numpy矩阵转换成字符形式，以便在网络中传输
        img_Data = data.tostring()

        # 先发送要发送的数据的长度
        # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
        conn.send(str.encode(str(len(img_Data)).ljust(16)))
        # # print(img_Data)
        # # 发送数据
        conn.send(img_Data)

        if cv2.waitKey(10) & 0xff == 27:
            break

    s.close()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ReceiveVideo()
