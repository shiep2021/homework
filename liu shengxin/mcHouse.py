from mcpi.minecraft import Minecraft
from datetime import datetime
from datetime import timedelta
import time
mc=Minecraft.create()

class House():
    def __init__(self,name,x0,y0,z0,l,w,h):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.z0=z0
        self.l=l
        self.w=w
        self.h=h
        self.stay_time = 0
    def buildWall(self):
        '''Build wall'''
        for y in range(self.h):
            if y%2==1:
                m=46
            else:
                m=1
            for x in range(self.l):
                mc.setBlock(self.x0+x,self.y0+y,self.z0,m)
                mc.setBlock(self.x0+x,self.y0+y,self.z0+self.w,m)
            for z in range(self.w):
                mc.setBlock(self.x0,self.y0+y,self.z0+z+1,m)
                mc.setBlock(self.x0+self.l-1,self.y0+y,self.z0+z+1,m)
    def buildFloor(self):
        '''Build floor in wool(blockId is 35)'''
        for x in range(self.l):
            for z in range(self.w+1):
                mc.setBlock(self.x0+x,self.y0,self.z0+z,35,2)
    def buildRoof(self):
        '''Build roof in glass(blockId is 20)'''
        for x in range(self.l):
            for z in range(self.w+1):
                mc.setBlock(self.x0+x,self.y0+self.h,self.z0+z,20)
    def buildDoor(self):
        '''Build door in the middle of x(air is 0)'''
        mc.setBlock(self.x0+self.l//2,self.y0+1,self.z0,0)
        mc.setBlock(self.x0+self.l//2,self.y0+2,self.z0,0)
        mc.setBlock(self.x0+self.l//2,self.y0+3,self.z0,0)
        mc.setBlock(self.x0 + self.l // 2+1, self.y0 + 1, self.z0, 0)
        mc.setBlock(self.x0 + self.l // 2+1, self.y0 + 2, self.z0, 0)
        mc.setBlock(self.x0 + self.l // 2+1, self.y0 + 3, self.z0, 0)
        mc.setBlock(self.x0 + self.l // 2 + 2, self.y0 + 1, self.z0, 0)
        mc.setBlock(self.x0 + self.l // 2 + 2, self.y0 + 2, self.z0, 0)
        mc.setBlock(self.x0 + self.l // 2 + 2, self.y0 + 3, self.z0, 0)
    def isInsidehouse(self,user):
        if user.x < self.x0+self.l and user.x > self.x0 and user.y < self.y0+self.h and  user.y > self.y0 and user.z < self.z0+self.w and user.z > self.z0: #判断是否在房间内
            self.stay_time += 1 #判断所在的时间
            mc.postToChat(f"Stay_time:{self.stay_time}") #聊天框显示待的时间
            if self.stay_time == 15:  #15s后打印其所在的房间
                mc.postToChat(f"welcome to the {self.name} house")
        else:
            self.stay_time = 0 #当离开房间时用户待在房间的时间清0
        #print(user.x,user.y,user.z)
        #print(self.x0,self.y0,self.z0)


if __name__ =="__main__":
    pos=mc.player.getTilePos()
    house1=House("peter",pos.x,pos.y,pos.z,10,6,15)
    house2=House("tom",pos.x+20,pos.y,pos.z,10,6,15)

    house1.buildFloor()