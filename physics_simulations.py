import pygame as py

from particle import Particle  # the individual particles on screen

"""
Class to handle the simulations of the engine (i.e dropping and react to player movements)

has private attrs:
    window {window to draw objects on}
    object_array {the particle array (required to move the positions of particle in simulation)}
    simulation_type {whether we are dropping or moving or throwing the shape}
    drop_stage {the stage of the drop (can be 0 (drop not begun) 1 (drop begun and in downward motion) 2 (rebound has occurred))}
has methods:
    set_attrs {precondition-> window, simulation type (str), object_array (list)
                postcondition->no return value}
        - sets the attributes of the physics simulation
    drop_square {precondition-> object_array (list), postcondition->no return value}
        - drops the square until one of the lowest particles has reached height 450
"""
class Physics_Simulations():
    __window = None
    __object_array = None
    __simulation_type = None
    __drop_stage = None 

    def __init__(self):
        self.__object_array = list()
        self.__window = None
        self.__simulation_type = None
        self.__drop_stage = 0

    
    def set_attrs(self, window, simulation_type: str, object_array: list):
        self.__object_array = object_array
        self.__window = window
        self.__simulation_type = simulation_type
        self.__drop_stage = 0

    # method for handling the dropping of a square (inclusive of horizontal displacement)
    def drop_square(self, object_array: list):
        # dropping a square from the current position
        self.__object_array = object_array

        # checking if the lowest particle is at the bottom of the screen
        if(self.__object_array[0].get_points()[1] < 450):

            # moving the shape downwards
            for i in range(0, len(self.__object_array)):
                pos = tuple(self.__object_array[i].get_points())
                self.__object_array[i].move_particle(pos[0], pos[1]+4)



    def get_shape_array(self)->list:
        return self.__object_array
    
    def set_shape_array(self, shape_array: list): self.__object_array = shape_array;
