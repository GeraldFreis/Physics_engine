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
from particle_movements import Particle_Movement

# testing the particle movements, specifically the horizontal flux of the particles to simulate the contraction and expansion of a soft body

# particles: current and past to resemble the node like behaviour of the material
current_particle = Particle(10, 250, 250); last_particle = Particle(10, 250, 240)
print(current_particle.get_points()[0])
# instantiating the Particle movement class
particle_mover = Particle_Movement(current_particle, last_particle)
particle_mover.calc_positions()

current_particle = particle_mover.get_particle();
print(current_particle.get_points()[0])