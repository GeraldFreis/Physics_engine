import pygame as py

from particle import Particle  # the individual particles on screen
from compression import Compression # the compression behaviours of the square
"""
Class to handle the simulations of the engine (i.e dropping and react to player movements)

has private attrs:
    window {window to draw objects on}
    object_array {the particle array (required to move the positions of particle in simulation)}
    simulation_type {whether we are dropping or moving or throwing the shape}
    drop_momentum_eq {int to hold the current movement}
has methods:
    set_attrs {precondition-> window, simulation type (str), object_array (list)
                postcondition->no return value}
        - sets the attributes of the physics simulation
    drop_square {precondition-> object_array (list), postcondition->no return value}
        - drops the square until one of the lowest particles has reached height 450
"""
class Physics_Simulations():
    __slots__ = ("__window", "__object_array","__simulation_type", "__drop_stage", "__drop_momentum_eq", "__momentum", "__top_offset",
    "__index_val", "under_compression", "compressed_object")

    def __init__(self):
        self.__object_array = list()
        self.__window = None
        self.__simulation_type = None
        self.__drop_stage = 0
        self.__drop_momentum_eq = "(-3x**4) - (1/9)(x**3) + 9(x**2) - x - 4"
        self.__momentum = 0
        self.__index_val = 0; # value that will hold the index of the current element which is increased every iteration
        self.under_compression = True
        self.compressed_object = Compression()
    
    def set_attrs(self, window, simulation_type: str, object_array: list)->None:
        self.__object_array = object_array
        self.__window = window
        self.__simulation_type = simulation_type

    # method for handling the dropping of a square (inclusive of horizontal displacement)
    def drop_square(self, object_array: list)->None:
        # dropping a square from the current position
        self.__object_array = object_array

        if(self.__drop_stage == 0): # if we are in the first stage of dropping the object
            if(self.__object_array[0].get_points()[1] <= 450):
                for i in range(0, len(self.__object_array)):
                    pos = tuple(self.__object_array[i].get_points())
                    self.__object_array[i].move_particle(pos[0], pos[1]+self.__momentum)    
                self.__momentum += 5 / 200
            else:
                self.compressed_object.set_object_array(self.__object_array)
                if(self.under_compression is True):
                    self.__object_array = self.compressed_object.compression_behaviour(self.__momentum, self.__index_val)
                    self.__index_val += 1
                    if(self.__index_val > 10):
                        self.under_compression = False
                else:
                    self.__drop_stage += 1
                    self.__momentum = -1.5

        elif(self.__drop_stage == 1):    # second stage (rebound) of the drop
            if(self.__object_array[0].get_points()[1] >= 390 and self.__object_array[0].get_points()[1] < 460):
                for i in range(0, len(self.__object_array)):
                    pos = tuple(self.__object_array[i].get_points())
                    self.__object_array[i].move_particle(pos[0], pos[1]+self.__momentum)   
                self.__momentum += 5 / 200
            else:
                self.__drop_stage += 1
                self.__momentum = 0


        elif(self.__drop_stage == 2): # final stage of the drop
            if(self.__object_array[0].get_points()[1] <= 450):
                for i in range(0, len(self.__object_array)):
                    pos = tuple(self.__object_array[i].get_points())
                    self.__object_array[i].move_particle(pos[0], pos[1]+self.__momentum)
                self.__momentum += 1.5 / 200
            else:
                self.__drop_stage += 1

        else: # if we have passed the drop stages
            pass;

    def set_stage(self, stage: int)->None:
        self.__drop_stage = stage

    def get_stage(self)->int:
        return self.__drop_stage


    def get_shape_array(self)->list:
        return self.__object_array
    
    def set_shape_array(self, shape_array: list): self.__object_array = shape_array;
