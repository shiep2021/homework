import vtk
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("1.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("2.stl")
mapper1= vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(reader1.GetOutputPort())
mapper2= vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(reader2.GetOutputPort()) 
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
renderer = vtk.vtkRenderer()
renderWindow=vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor=vtk.vtkRenderWindowInteractor() 
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.SetBackground(0,255,255)
actor1.SetOrigin(actor1.GetCenter())
actor2.SetOrigin(actor2.GetCenter())
actor1.GetProperty().SetColor(1,0,0)
actor2.GetProperty().SetColor(1,0,1)
print("actor1 center:",actor1.GetCenter())
print("actor2 center:",actor2.GetCenter())
for i in range(36000):
    actor1.RotateX(0.1)
    actor2.RotateY(0.1) 
    renderWindow.Render()
# import vtk
# reader1=vtk.vtkSTLReader()
# reader1.SetFileName("5.18.stl")
# reader2 = vtk.vtkSTLReader()
# reader2.SetFileName("2. stl") 
# mapper1=vtk.vtkPolyDataMapper()
# mapper1.SetInputConnection(reader1.GetOutputPort())
# mapper2= vtk.vtkPolyDataMapper()
# mapper2.SetInputConnection(reader2.GetOutputPort())
# actor1 = vtk.vtkActor()
# actor1.SetMapper(mapper1) 
# actor2 = vtk.vtkActor() 
# actor2.SetMapper(mapper2) 
# renderer = vtk.vtkRenderer()
# renderWindow = vtk.vtkRenderWindow() 
# renderWindow.AddRenderer(renderer)
# renderWindowInteractor=vtk.vtkRenderWindowInteractor() 
# renderWindowInteractor.SetRenderWindow(renderWindow) 
# renderer.AddActor(actor1)
# renderer.AddActor(actor2)
# renderer.SetBackground(0,0,0.8) 
# actor1.SetOrigin(actor1.GetCenter()) 
# actor2.SetOrigin(actor2.GetCenter())
# actor1.GetProperty().SetColor(1,0,0)
# for i in range(36000):
#     actor1.RotateZ(0.2) 
#     actor2.RotateZ(0.2)
#     renderWindow.Render()