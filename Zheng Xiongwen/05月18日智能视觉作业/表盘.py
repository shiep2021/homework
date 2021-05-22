import vtk
from datetime import datetime
import time
dt1 = datetime.now()
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("zuixinbiaopan.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("shizhen.stl")
reader3 = vtk.vtkSTLReader()
reader3.SetFileName("fenzhen.stl")
reader4 = vtk.vtkSTLReader()
reader4.SetFileName("miaozhen.stl")

mapper1 = vtk.vtkPolyDataMapper ()
mapper1.SetInputConnection (reader1.GetOutputPort())
mapper2 = vtk. vtkPolyDataMapper ()
mapper2.SetInputConnection(reader2.GetOutputPort())
mapper3 = vtk. vtkPolyDataMapper ()
mapper3.SetInputConnection(reader3.GetOutputPort())
mapper4 = vtk. vtkPolyDataMapper ()
mapper4.SetInputConnection(reader4.GetOutputPort())

actor1 = vtk. vtkActor ()
actor1.SetMapper (mapper1)
actor2 = vtk. vtkActor()
actor2.SetMapper (mapper2)
actor3 = vtk. vtkActor()
actor3.SetMapper (mapper3)
actor4 = vtk. vtkActor()
actor4.SetMapper (mapper4)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)

renderer.SetBackground(0,0,0.8)
actor1.SetOrigin(actor1.GetCenter())
actor2.SetOrigin(actor1.GetCenter())
actor3.SetOrigin(actor1.GetCenter())
actor4.SetOrigin(actor1.GetCenter())

actor1.GetProperty().SetColor(135/255,158/255,172/255)
actor2.GetProperty().SetColor(127/255,255/255,212/255)
actor3.GetProperty().SetColor(127/255,255/255,212/255)
actor4.GetProperty().SetColor(127/255,255/255,212/255)

actor1.RotateZ(-90)
actor2.RotateZ(-90)
actor3.RotateZ(-90)
actor4.RotateZ(-90)

# print(dt1.hour)               #时
# print(dt1.minute)             #分
# print(dt1.second)             #秒
if dt1.hour <=12 :
    dt1.hour += 12
actor2.RotateZ(-(dt1.hour-12)*30)
actor3.RotateZ(-dt1.minute*6)
actor4.RotateZ(-dt1.second*6)

while True:
    lasttimesecond = datetime.now().second
    # lasttimeminute = datetime.now().minute
    # lasttimehour = datetime.now().hour
    time.sleep(1)
    # start = time.time()
    miaozhenjiaodu = -abs(datetime.now().second-lasttimesecond) * 6
    # fenzhenjiaodu = -abs(datetime.now().minute - lasttimeminute) * 6
    # shizhenjiaodu = -abs(datetime.now().hour - lasttimehour) * 30
    actor2.RotateZ(miaozhenjiaodu/3600)
    actor3.RotateZ(miaozhenjiaodu/60)
    actor4.RotateZ(miaozhenjiaodu)
    renderWindow.Render()
    # print(time.time()-start)
