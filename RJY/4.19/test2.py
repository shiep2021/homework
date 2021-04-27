from mcHouse import House
from mcpi.minecraft import Minecraft
from  time import sleep


mc=Minecraft.create()
pos=mc.player.getTilePos()

house1=House("xiaoli",pos.x,pos.y,pos.z,10,6,15)
house2=House("xiaohua",pos.x+20,pos.y+20,pos.z+20,10,6,15)

house1.buildWall()
house1.buildFloor()
house1.buildRoof()
house1.buildDoor()
house2.buildWall()
house2.buildFloor()
house2.buildRoof()
house2.buildDoor()



while True:
    pos = mc.player.getTilePos()  
    house1.isInsidehouse(pos)
    house2.isInsidehouse(pos)
    sleep(1)