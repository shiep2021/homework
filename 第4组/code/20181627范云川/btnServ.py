import mySerial as se
import tkinter
#串口连接
com= se.comPorts(0)
a=se.MXSerial(com,9600)

def open():
    a.send("2a")
def close():
    a.send("3a")
top=tkinter.Tk()
top.title("发射控制器")
btn=tkinter.Button(top,text="开启",command=open)
btn.place(x=60,y=40)
btn=tkinter.Button(top,text="关闭",command=close)
btn.place(x=120,y=40)
tkinter.Label(top,text='火箭发射控制器',font=('Arial',14)).place(x=50,y=10)
top.mainloop()