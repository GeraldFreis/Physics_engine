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
from draw_shapes import Draw_shapes_2D

def testing_horizontal_displacement_static():
	# testing the particle movements, specifically the horizontal flux of the particles to simulate the contraction and expansion of a soft body
	print("Testing static particles\n\n")
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

def testing_horizontal_displacement_list():
	"""Test 2 -> 10 (testing the movement with more than 2 particles)"""
	print("\nTesting a list of particles\n\n");

	# using a for loop
	global normal_x
	normal_x = 250
	N_y = 250

	particle_list = list(); # list to contain the particles

	# filling the particle list with 10 particles
	for i in range(10):
		N_y += 10
		particle_list.append(Particle(10, normal_x, N_y))

	particle_mover = Particle_Movement(particle_list[1], particle_list[0])

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
			print("Test "+ str(i + 1) +" passed")
			print(particle_list[i].get_points()[0], particle_list[i-1].get_points()[0])
			print("\n")

def testing_horizontal_displacement_realistic():
	"""Setting up the particles as they are in the game"""
	# this includes getting only the side particles to flex

	shapes_arr = Draw_shapes_2D()
	shapes_arr.creating_shape_array_square(10) # creating the square of side length 10
	particle_list = shapes_arr.get_shape_array() # getting the array of particles (list form)

	particle_mover = Particle_Movement(particle_list[1], particle_list[0])

	print("\nTesting particles as set up in engine\n\n")

	# moving all vals on the left of the square
	for i in range(1, 10):
		particle_mover.set_particles(particle_list[i], particle_list[i-1])
		particle_mover.calc_positions()
		particle_list[i] = particle_mover.get_particle()

	# testing the particles
	for i in range(1, 10):
		if(particle_list[i].get_points()[0] != (particle_list[i-1].get_points()[0]+5)):
			print("Test "+ str(i + 10) + " failed\n")
		else:
			print("Test "+ str(i + 10) +" passed")
			print(particle_list[i].get_points()[0], particle_list[i-1].get_points()[0])
			print("\n")

	# moving all vals on the right side of the square
	for i in range(21, 30):
		particle_mover.set_particles(particle_list[i], particle_list[i-1])
		particle_mover.calc_positions()
		particle_list[i] = particle_mover.get_particle()

	for i in range(21, 30):
		if(particle_list[i].get_points()[0] != (particle_list[i-1].get_points()[0]-5)):
			print("Test "+ str(i + 1) + " failed\n")
		else:
			print("Test "+ str(i + 1) +" passed")
			print(particle_list[i].get_points()[0], particle_list[i-1].get_points()[0])
			print("\n")

testing_horizontal_displacement_static()
testing_horizontal_displacement_list()
testing_horizontal_displacement_realistic()
