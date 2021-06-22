import socket
from time import ctime
HOST='192.168.136.61'
PORT=21567      
BUFSIZE=1024
ADDR=(HOST,PORT)

serversocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen(5)

while True:
    print("waiting for connecting....")
    clientsocket,addr = serversocket.accept()
    print("...connnected from : %s" % str(addr))

    while True:
        data= clientsocket.recv(BUFSIZE)

        if not data:
            break
        data =data.decode('utf-8')
        if data =='H':
            clientsocket.send(bytes(123))
        else:
            #respMsg="[%s] liu %s"%(ctime(),data)
            print(data)
            #clientsocket.send(bytes(respMsg,'utf-8'))

    clientsocket.close()


serversocket.close()