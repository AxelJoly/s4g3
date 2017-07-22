import bpy
import os

from mathutils import Vector

class Curve(object):
    
    def __init__(self):
        self.array_vector = []
        
    def load_data(self, filename):
        with open(filename, 'r') as file:
            points = [(float(coordinate) for coordinate in line.split()) for line in  file]
            self.array_vector = [Vector(x)*2 for x in points]

        # print(self.array_vector)
    
    def delete_data(self):
        self.array_vector = []
    
    def draw(self):
        len_array_vector = len(self.array_vector)
        
        curvedata = bpy.data.curves.new(name="curve_name", type='CURVE')  
        curvedata.dimensions = '3D'  
      
        objectdata = bpy.data.objects.new("Curve", curvedata)  
        objectdata.location = (0,0,0)
        bpy.context.scene.objects.link(objectdata)  
      
        polyline = curvedata.splines.new('NURBS')  
        polyline.points.add(len_array_vector-1)
        
        for num in range(len_array_vector):  
            x, y, z = self.array_vector[num]  
            polyline.points[num].co = (x, y, z, 1)  
      
        polyline.order_u = len(polyline.points)-1
        polyline.use_endpoint_u = True
        polyline.use_cyclic_u = True 

    def add_track(self, filename):
        models_path = os.path.join(base_path, "Models", filename)
    
        imported_object = bpy.ops.import_scene.obj(filepath=models_path)
        rail = bpy.context.selected_objects[0]
        rail.name = "Rail"
        rail.dimensions = (rail.dimensions/10)
        
        bpy.context.scene.objects.active = rail
        
        bpy.ops.object.modifier_add(type='ARRAY')
        
        bpy.context.object.modifiers['Array'].count = 20
        bpy.ops.object.modifier_add(type='CURVE')
        bpy.context.object.modifiers['Curve'].object = bpy.data.objects['Curve']
        
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array")
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Curve")

def remove_all_objects():
    for o in bpy.data.objects:
        o.select = True
    
    bpy.ops.object.delete()

if __name__ == "__main__":
    os.system('cls')

    #try:
    #    objs = bpy.data.objects
    #    objs.remove(objs["Rail"], True)
    #    objs.remove(objs["Curve"], True)
    #except:
    #    pass
    
    #base_path = os.path.dirname(os.path.dirname(__file__)) # base_path
    #data_path = os.path.join(base_path, "Data", "data_test")
    
    #curve = Curve()
    #curve.load_data(data_path)
    #curve.draw()
    #curve.add_track("rail.obj")
    
    
        