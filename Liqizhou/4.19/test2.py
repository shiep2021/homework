from House import House
from mcpi.minecraft import Minecraft
from  time import sleep


mc=Minecraft.create()
pos=mc.player.getTilePos()

#创建了2个房子对象，并创建了墙、地板、屋顶和门
house1=House("Lacus",pos.x,pos.y,pos.z,10,6,15)
house2=House("moli",pos.x+20,pos.y+20,pos.z+20,10,6,15)

house1.buildWall()
house1.buildFloor()
house1.buildRoof()
house1.buildDoor()
house2.buildWall()
house2.buildFloor()
house2.buildRoof()
house2.buildDoor()



while True:
    pos = mc.player.getTilePos()  #读取用户的位置
    #判断用户是否在房间
    house1.isInsidehouse(pos)
    house2.isInsidehouse(pos)
    sleep(1)