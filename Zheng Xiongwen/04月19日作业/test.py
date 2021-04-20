from mcHouse import House
from mcpi.minecraft import Minecraft
from  time import sleep


mc=Minecraft.create()
pos=mc.player.getTilePos()

#创建了2个房子对象，并创建了墙、地板、屋顶和门
'''house1=House("peter",pos.x,pos.y,pos.z,10,6,15)
house2=House("tom",pos.x+20,pos.y+20,pos.z+20,10,6,15)
house3=House("mike",pos.x+40,pos.y+40,pos.z+40,10,6,15)

house1.buildWall()
house1.buildFloor()
house1.buildRoof()
house1.buildDoor()
house2.buildWall()
house2.buildFloor()
house2.buildRoof()
house2.buildDoor()
house3.buildWall()
house3.buildFloor()
house3.buildRoof()
house3.buildDoor()'''

stay_time = 0

number = eval(input("请输入房子的个数:"))
for i in range(1,number+1):
    name = input(f"请输入房子{i}的所有者:")
    x0, y0, z0, l, w, h = list(map(int,input("请输入该房子的各个属性(顺序为x,y,z,l,w,h),并以空格分隔:").split()))
    locals()['house' + str(i)] = House(name, pos.x + x0, pos.y + y0, pos.z + z0, l, w, h)
    house = locals()['house' + str(i)]
    house.buildWall()
    house.buildFloor()
    house.buildRoof()
    house.buildDoor()

while True:
    pos = mc.player.getTilePos()  #读取用户的位置
    #判断用户是否在房间
    for i in range(1,number+1):
        locals()['house' + str(i)].isInsidehouse(pos)
    #house2.isInsidehouse(pos)
    #house3.isInsidehouse(pos)
    sleep(1)