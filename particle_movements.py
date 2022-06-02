from particle import Particle

"""
Class to calculate the particle movements, given the current particle and the last particle
has attrs:
    current particle and under particle but both are private:
        -> can be set with the set particles function, given the particles as formal parameters
has methods:
    set_particles
    get_particles
    calc_positions
"""
class Particle_Movement():
    # the private attrs
    __current_particle = None
    __under_particle = None

    def __init__(self, this_particle: Particle, last_particle: Particle):
        self.__current_particle = this_particle
        self.__under_particle = last_particle
    
    # setting the particles to be moved
    def set_particles(self, this_particle: Particle, last_particle: Particle):
        self.__current_particle = this_particle
        self.__under_particle = last_particle
    
    # returning the particles (self and current as a tuple)
    def get_particles(self)->Particle:
        return self.__current_particle
    
    # calculate the positions of the particles based on the movement and direction of the previous particle
    def calc_positions(self):
        # how do I want to do this?
        print("here")