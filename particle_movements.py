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
    __reverse_flux = None

    def __init__(self, this_particle: Particle, last_particle: Particle):
        self.__current_particle = this_particle
        self.__under_particle = last_particle
        self.__reverse_flux = False
    
    # setting the particles to be moved
    def set_particles(self, this_particle: Particle, last_particle: Particle):
        self.__current_particle = this_particle
        self.__under_particle = last_particle
    
    # returning the particles (self and current as a tuple)
    def get_particle(self)->Particle:
        return self.__current_particle
    
    # calculate the positions of the particles based on the movement and direction of the previous particle
    def calc_positions(self):

        # getting the x positions of the current particle and the particle above
        current_x = self.__current_particle.get_points()[0]; last_x = self.__under_particle.get_points()[0]

        if(self.__reverse_flux is not True): # if we are moving each particle inward
            if(current_x < 300): # if the particle is not past the central point (where flux is at max (or g'(t) = 0 && f'(t) != 0){if treated as parametric})
                current_x = last_x + 5

            else: # if we are past the central x position we must reverse
                self.__reverse_flux = True # reversing the direction

        else: # if we need to move the items backwards
            if(current_x > 250): # if we are greater than the minimal x position
                current_x = last_x - 5

            else:
                self.__reverse_flux = False

        # updating the current particles position
        self.__current_particle.move_particle(current_x, self.__current_particle.get_points()[1]);

    def get_flux()->bool: return self.__reverse_flux
