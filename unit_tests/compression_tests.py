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
    comp = Compression()
    simulation = Physics_Simulations()
    simulation.drop_square(shape_array)
    shape_array = simulation.get_shape_array()