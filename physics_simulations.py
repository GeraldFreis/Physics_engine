import pygame as py
from particle import Particle # the individual particles on screen 

class Physics_Simulations():
    __window = None
    __object_array = None
    __simulation_type = None

    def __init__(self):
        self.__object_array = list()
        self.__window = None
        self.__simulation_type = None

    
    def set_attrs(self, window, simulation_type: str, object_array: list):
        self.__object_array = object_array
        self.__window = window
        self.__simulation_type = simulation_type

    # method for dropping a square
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