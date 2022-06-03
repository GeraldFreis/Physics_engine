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

def testing_horizontal_displacement():
	# testing the particle movements, specifically the horizontal flux of the particles to simulate the contraction and expansion of a soft body

	"""Test 1 (testing the movement with two particles"""
	# particles: current and past to resemble the node like behaviour of the material
	current_particle_x = 250; last_particle_x = 240
	current_particle = Particle(10, current_particle_x, 250); last_particle = Particle(10, last_particle_x, 240)

	# instantiating the Particle movement class
	particle_mover = Particle_Movement(current_particle, last_particle)
	particle_mover.calc_positions()

	current_particle = particle_mover.get_particle();
	if(current_particle.get_points()[0] != (last_particle_x + 5)):
		print("Test 1 failed (current particle did not move correctly)\n")
	else:
		print("Test 1 passed\n")

	"""Test 2 (testing the movement with more than 2 particles)"""
	# using a for loop
	global normal_x
	normal_x = 250
	N_y = 250

	particle_list = list(); # list to contain the particles

	# filling the particle list with 10 particles
	for i in range(10):
		N_y += 10
		particle_list.append(Particle(10, normal_x, N_y))

	# moving each of those particles in the normal fashion
	for i in range(1, 10):
		particle_mover.set_particles(particle_list[i], particle_list[i-1])
		particle_mover.calc_positions();
		particle_list[i] = particle_mover.get_particle()

	# testing each particle
	for i in range(1, 10):
		if(particle_list[i].get_points()[0] != (particle_list[i-1].get_points()[0]+5)):
			print("Test "+ str(i + 1) + " failed\n")
		else:
			print("Test "+ str(i + 1) +" passed\n")
			print(particle_list[i].get_points()[0], particle_list[i-1].get_points()[0])

testing_horizontal_displacement()
