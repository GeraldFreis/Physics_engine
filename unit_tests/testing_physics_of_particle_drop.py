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
from particle_movements.py import Particle_movements

# testing the particle movements

