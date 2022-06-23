import pygame as py
from particle import Particle
"""Utility Class to draw 2 dimensional shapes onto the screen
    Methods:
        draw_crcle(self, radius): takes radius (int) as a parameter and returns true if a shape was drawn
        draw_square(self, sidelength): takes length as parameters and returns true if the shape was drawn
        draw_rectangle(self, width, height): validates that it is a  rectangle and then draws the shape """
class Draw_shapes_2D(): 
    __object_array = None

    def __init__(self):
        self.__object_array = list() # initialising the object array
        
    # draws a Square
    def draw_circle(self, radius):
        return 0;

    # draws a square
    def draw_square(self, sidelength: int, window):
        # drawing every Particle onto the screen
        for obj in range (0, sidelength*4):
            self.__object_array[obj].draw_particle(window)

    def creating_shape_array_square(self, sidelength:int):
        if(len(self.__object_array) == 0):
            y_pos = 250; x_pos = 250

            # Particle 0 -> side length-1 is in range (250, 350) -> (250, 350-(17 * sidelength))
            for obj in range(0, sidelength):
                self.__object_array.append(Particle(10, x_pos, y_pos))
                y_pos -= 17

            # Particle sidelength to 2 * sidelength is in range(250, 350 - (17*sidelength)) -> (250 + (17 * sidelength), 350 - (17*sidelength))
            for obj in range(0, sidelength):
                self.__object_array.append(Particle(10, x_pos, y_pos))
                x_pos += 17
            
            # Particle sidelength * 2 to sidelength * 3 is in range (250+17*sidelength, 350-17*sidelength) -> (250+17*sidelength, 350)
            for obj in range(0, sidelength):
                self.__object_array.append(Particle(10, x_pos, y_pos))
                y_pos += 17

            # Particle sidelength * 3 to sidelength * 4 is in range (250+15*sidelength, 350) -> (250, 350)
            for obj in range(0, sidelength):
                self.__object_array.append(Particle(10, x_pos, y_pos))
                x_pos -= 17
        
        
    def draw_square_if_initialised(self, window):
        try:
            for obj in range (0, len(self.__object_array)):
                self.__object_array[obj].draw_particle(window)
        except IndexError and AttributeError:
            print("No vals in object array (draw_shapes.py line 55)\n")
        

    def set_shape_array(self, shape_array: list):
        self.__object_array = shape_array
    
    # draws a rectangle
    def draw_rectangle(self, width, height):
        return 0
    
    def get_shape_array(self)->list:
        return self.__object_array
    