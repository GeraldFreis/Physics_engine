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

# testing the drop_square function in the Physics_simulations class
def testing_drop(shape_array: list):
    # testing if the points are added correctly in a static setting (manual incrementation)
    initial_point = shape_array[0].get_points()
    simulation = Physics_Simulations()
    simulation.drop_square(shape_array)
    shape_array = simulation.get_shape_array()
    final_point = shape_array[0].get_points()

    if(final_point[1] == initial_point[1] + 17):
        print("Test 1 passed", final_point[1])
    else:
        print("Test 1 failed", final_point[1])
    
    # testing if the points are added correctly in a dynamic / auto setting
    initial_point = final_point

    for i in range(0, 5):
        simulation = Physics_Simulations()
        simulation.drop_square(shape_array)
        shape_array = simulation.get_shape_array()
    
    final_point = shape_array[0].get_points()

    if(final_point[1] == initial_point[1] + 17*5):
        print("Test 2 passed", final_point[1])
    else:
        print("Test 2 failed", final_point[1])
    
    # testing if the points are added correctly in a while loop

    while(shape_array[0].get_points()[1] < 620):
        simulation = Physics_Simulations()
        simulation.drop_square(shape_array)
        shape_array = simulation.get_shape_array()
    
    if(shape_array[0].get_points()[1] < 700):
        print("Test 3 passed", shape_array[0].get_points()[1])
    else:
        print("Test 3 failed", shape_array[0].get_points()[1])
