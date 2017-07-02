import bpy
from random import randint
from mathutils import Vector
from bpy_extras.io_utils import unpack_list
import os

os.system('cls')

for obj in bpy.data.objects:
    obj.select = True
    
bpy.ops.object.delete()


filepath = "//dog.blend"

# append all objects starting with 'house'
#with bpy.data.libraries.load(filepath) as (data_from, data_to):
#    data_to.objects = [name for name in data_from.objects]

#print(data_to.objects)
# link them to scene
#scene = bpy.context.scene
#for obj in data_to.objects:
#    if obj is not None:
#        scene.objects.link(obj)

# Version 1

points = [(0,2,0),(2,3,0),(3,2,0),(4,0,0),(3,-2,0),(1,-3,0),(-1,-3,0),(-2,-2,0),(-3,-3,0),(-5,-2,0),(-4,0,0),(-3,2,0)]

curvedata = bpy.data.curves.new(name="Curve", type='CURVE')

curvedata.dimensions = '3D'
curvedata.fill_mode = 'FULL' 

ob = bpy.data.objects.new("CurveObj", curvedata)
bpy.context.scene.objects.link(ob)

spline = curvedata.splines.new('BEZIER')

spline.bezier_points.add(len(points)-1)
spline.bezier_points.foreach_set("co", unpack_list(points))
spline.use_cyclic_u = True  

# Version 2

w = 1 # weight  
p = [Vector(x) for x in points]
  
def MakePolyLine(objname, curvename, cList):  
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')  
    curvedata.dimensions = '3D'  
  
    objectdata = bpy.data.objects.new(objname, curvedata)  
    objectdata.location = (0,0,0) #object origin  
    bpy.context.scene.objects.link(objectdata)  
  
    polyline = curvedata.splines.new('NURBS')  
    polyline.points.add(len(cList)-1)  
    for num in range(len(cList)):  
        x, y, z = cList[num]  
        polyline.points[num].co = (x, y, z, w)  
  
    polyline.order_u = len(polyline.points)-1
    polyline.use_endpoint_u = True
    polyline.use_cyclic_u = True    
  
MakePolyLine("NameOfMyCurveObject", "NameOfMyCurve", p)