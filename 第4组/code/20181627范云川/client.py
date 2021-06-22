import socket
import cv2
import numpy as np
import sys

def recvall(sock, count):
    buf = b''  # buf是一个byte类型
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def SendVideo():
    # 建立sock连接
    # address要连接的服务器IP地址和端口号
    address = ('10.56.21.13', 2345)
    try:
        # 建立socket对象，参数意义见https://blog.csdn.net/rebelqsp/article/details/22109925
        # socket.AF_INET：服务器之间网络通信
        # socket.SOCK_STREAM：流式socket , for TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 开启连接
        sock.connect(address)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    # 建立图像读取对象
    capture = cv2.VideoCapture(0)

    capture.set(3, 1280)
    capture.set(4, 480)
    # 读取一帧图像，读取成功:ret=1 frame=读取到的一帧图像；读取失败:ret=0
    ret, frame = capture.read()
    # 压缩参数，后面cv2.imencode将会用到，对于jpeg来说，15代表图像质量，越高代表图像质量越好为 0-100，默认95
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]

    while ret:
        # cv2.imencode将图片格式转换(编码)成流数据，赋值到内存缓存中;主要用于图像数据格式的压缩，方便网络传输
        # '.jpg'表示将图片按照jpg格式编码。
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        # 建立矩阵
        data = np.array(imgencode)
        # 将numpy矩阵转换成字符形式，以便在网络中传输
        stringData = data.tostring()
        # 先发送要发送的数据的长度
        # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
        sock.send(str.encode(str(len(stringData)).ljust(16)))
        # 发送数据
        sock.send(stringData)
        # 读取服务器返回值
        receive = sock.recv(16)
        if len(receive):
            stringData = recvall(sock,int(receive))
            data = np.frombuffer(stringData, np.uint8)
            image = cv2.imdecode(data, cv2.IMREAD_COLOR)
            #cv2.imshow('show', image)
        # 读取下一帧图片
        ret, frame = capture.read()
        # cv2.imshow('show', frame)
        if cv2.waitKey(10) == 27:
            break
    sock.close()


if __name__ == '__main__':
    SendVideo()
