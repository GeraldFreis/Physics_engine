from particle import Particle
import pygame as py
from draw_shapes import Draw_shapes_2D

"""This class will call the drawing shape functions from the draw shapes utility class"""
class Shape():
    __shape_type = None
    __drop_begun = None
    __shape_array = None

    def __init__(self):
        self.__shape_type = "circle"
        self.__drop_begun = False
        self.__shape_array = list()
        self.drawing_shapes = Draw_shapes_2D()
    
    # function to draw shapes onto the screen
    def draw_shape(self, window):
        # for the time being this is just going to be how we manually draw the shapes
        if(self.__drop_begun is False):
            self.drawing_shapes.creating_shape_array_square(10)
            self.__shape_array = self.drawing_shapes.get_shape_array()
            self.drawing_shapes.draw_square(10, window)
            self.__drop_begun = True
        else:
            self.drawing_shapes.set_shape_array(self.__shape_array)
            self.drawing_shapes.draw_square_if_initialised(window)
        return
    
    # making a shape array if it needs a square
    def make_shape_array_square(self):
        self.drawing_shapes.creating_shape_array_square(10)
        self.__shape_array = self.drawing_shapes.get_shape_array()
        self.__drop_begun = True
    
    def get_drop(self)->bool: return self.__drop_begun

    def set_drop(self, drop_state: bool): self.__drop_begun = drop_state

    def set_shape_array(self, shape_array: list): self.__shape_array = shape_array

    def get_shape_array(self)->list: return self.__shape_array
    