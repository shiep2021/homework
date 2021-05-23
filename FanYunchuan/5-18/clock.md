![clock](https://user-images.githubusercontent.com/55586349/119253514-23a6be80-bbe4-11eb-966e-cb9dccb18592.png)


import vtk
import time
from datetime import datetime 

dt1 = datetime.now()

reader_clock = vtk.vtkSTLReader()
reader_clock.SetFileName("clock.stl")
reader_hour = vtk.vtkSTLReader()
reader_hour.SetFileName("hour.stl")
reader_min = vtk.vtkSTLReader()
reader_min.SetFileName("min.stl")
reader_sec = vtk.vtkSTLReader()
reader_sec.SetFileName("sec.stl")

mapper_clock = vtk.vtkPolyDataMapper()
mapper_clock.SetInputConnection(reader_clock.GetOutputPort())
mapper_hour = vtk.vtkPolyDataMapper()
mapper_hour.SetInputConnection(reader_hour.GetOutputPort())
mapper_min = vtk.vtkPolyDataMapper()
mapper_min.SetInputConnection(reader_min.GetOutputPort())
mapper_sec = vtk.vtkPolyDataMapper()
mapper_sec.SetInputConnection(reader_sec.GetOutputPort())

actor_clock = vtk.vtkActor()
actor_clock.SetMapper(mapper_clock)
actor_hour = vtk.vtkActor()
actor_hour.SetMapper(mapper_hour)
actor_min = vtk.vtkActor()
actor_min.SetMapper(mapper_min)
actor_sec = vtk.vtkActor()
actor_sec.SetMapper(mapper_sec)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor_min)
renderer.AddActor(actor_clock)
renderer.AddActor(actor_hour)
renderer.AddActor(actor_sec)

#设置背景色
renderer.SetBackground(0,0,0)

#设置实体中心
actor_clock.SetOrigin(actor_clock.GetCenter())
actor_hour.SetOrigin(actor_clock.GetCenter())
actor_min.SetOrigin(actor_clock.GetCenter())
actor_sec.SetOrigin(actor_clock.GetCenter())
print("actor_clock center",actor_clock.GetCenter())
print("actor_hour center",actor_hour.GetCenter())
print("actor_min center",actor_min.GetCenter())


actor_clock.GetProperty().SetColor(135/255,158/255,172/255)
actor_hour.GetProperty().SetColor(127/255,255/255,212/255)
actor_min.GetProperty().SetColor(127/255,255/255,212/255)
actor_sec.GetProperty().SetColor(127/255,255/255,212/255)

#初始12点钟Z轴旋转-90°/6点钟方向旋转90°
actor_clock.RotateZ(-90)
actor_hour.RotateZ(-90)
actor_min.RotateZ(-90)
actor_sec.RotateZ(-90)

#初始角度
if dt1.hour <=12 :
    dt1.hour += 12
actor_hour.RotateZ(-(dt1.hour-12)*30)
actor_min.RotateZ(-dt1.minute*6)
actor_sec.RotateZ(-dt1.second*6)

while True:
    flag = datetime.now().second
    time.sleep(1)
    angle_sec = -abs(datetime.now().second-flag) * 6
    actor_hour.RotateZ(angle_sec/3600)
    actor_min.RotateZ(angle_sec/60)
    actor_sec.RotateZ(angle_sec)
    renderWindow.Render()
