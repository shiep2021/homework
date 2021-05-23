import vtk
reader1 = vtk.vtkSTLReader()
reader1.SetFileName("zhong.stl")
reader2 = vtk.vtkSTLReader()
reader2.SetFileName("shizhen1.stl")
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
renderer.SetBackground(0,0,255)
actor1.SetOrigin(actor1.GetCenter())
actor2.SetOrigin(actor1.GetCenter())
actor1.GetProperty().SetColor(1,1,1)
actor2.GetProperty().SetColor(0,0,0)
while True:
    actor2.RotateZ(-0.1)
    renderWindow.Render()