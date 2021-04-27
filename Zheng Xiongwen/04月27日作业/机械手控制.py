import time
import LeArm
import LeCmd
import LeConf

import tkinter
top = tkinter.Tk()
top.title("电力大学")

# 偏差+初始化
if not len(LeConf.Deviation) == 6:
    print("偏差数量错误")
    sys.exit()
else:
    d = []
    for i in range(0, len(LeConf.Deviation), 1):
        if LeConf.Deviation[i] > 1800 or LeConf.Deviation[i] < 1200:
            print("偏差值超出范围1200-1800")
            sys.exit()
        else:
            d.append(LeConf.Deviation[i] - 1500)
LeArm.initLeArm(tuple(d))

def jiandao():
    LeArm.runActionGroup('6_2_23', 1) #剪刀
def shitou():
    LeArm.runActionGroup('0_0_0', 1) #石头
def bu():
    LeArm.runActionGroup('15_5_12345', 1) #布
btn = tkinter.Button(top,text="剪刀",command=jiandao)
btn.place(x=40,y=60)
btn = tkinter.Button(top,text="石头",command=shitou)
btn.place(x=100,y=60)
btn = tkinter.Button(top,text="布",command=bu)
btn.place(x=160,y=60)

tkinter.Label(top, text='机械手控制模拟器',font=('Arial',12)).place(x=50,y=30)
top.mainloop()



