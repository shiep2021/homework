import vtk
reader = vtk.vtkSTLReader()
reader.SetFileName("1.stl")
mapper= vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort()) 
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer = vtk.vtkRenderer()
renderWindow=vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor=vtk.vtkRenderWindowInteractor() 
renderWindowInteractor.SetRenderWindow(renderWindow) 
print("actor1 center:",actor.GetCenter())
renderer.AddActor(actor)
renderer.SetBackground(0,125,125)
#actor.SetOrigin(actor.GetCenter())
actor.SetOrigin(-160,125,1.0)
for i in range(36000):
    actor.RotateZ(0.2) 
    renderWindow.Render()
    

