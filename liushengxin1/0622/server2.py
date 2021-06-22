import socket
from time import ctime
HOST='192.168.136.62'
PORT=21567      
BUFSIZE=1024
ADDR=(HOST,PORT)

serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen(5)

import serial

serialPort = "COM28"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

demo1=b"0"#将0转换为ASCII码方便发送
demo2=b"1"#同理

while True:
    print("waiting for connecting....")
    clientsocket,addr = serversocket.accept()
    print("...connnected from : %s" % str(addr))

    while True:
        data= clientsocket.recv(BUFSIZE)

        if not data:
            break
        data =data.decode('utf-8')
        if data =='0':
            respMsg='已收到'
            clientsocket.send(bytes(respMsg,'utf-8'))
            ser.write(demo1)
        if data == '1':
            respMsg='已收到'
            clientsocket.send(bytes(respMsg,'utf-8'))
            ser.write(demo2)

    clientsocket.close()


serversocket.close()