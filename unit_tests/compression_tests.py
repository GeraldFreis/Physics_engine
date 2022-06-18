import path
import sys
  
# directory reach
directory = path.Path(__file__).abspath()
  
# setting path
sys.path.append(directory.parent.parent)
  
from shapes import Shape
import pygame as py
from physics_simulations import Physics_Simulations
from particle import Particle
from compression import Compression

def tests():
    shape_obj = Shape()
    shape_obj.make_shape_array_square() # making the shape array
    shape_array = shape_obj.get_shape_array()
    comp = Compression()
    simulation = Physics_Simulations()
    simulation.drop_square(shape_array)
    shape_array = simulation.get_shape_array()
    
    for i in range(len(shape_array)):
        print(shape_array[i].get_points()[0], shape_array[i].get_points()[1], i)
    
    print("\n")

    comp.set_object_array(shape_array)
    for i in range(9):
        shape_array = comp.compression_behaviour(5, i)
        comp.set_object_array(shape_array)

    for i in range(len(shape_array)):
        print(shape_array[i].get_points()[0], shape_array[i].get_points()[1], i)
    

tests()