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
from drop_square_tests import testing_drop

if __name__ == "__main__":
    shape_obj = Shape()
    shape_obj.make_shape_array_square() # making the shape array

    testing_drop(shape_obj.get_shape_array());
