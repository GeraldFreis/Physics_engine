import pygame as py

"""Class to handle the particles on the screen"""
class Particle():
    __radius = None
    __x = None
    __y = None
    __momentum = None

    # constructors
    def __init__(self):
        self.__radius = 0
        self.__momentum = tuple()
    
    def __init__(self, radius: int, x: int, y: int):
        self.__radius = radius
        self.__x = x
        self.__y = y
        self.__momentum = tuple() # direction 

    # methods
    def move_particle(self, new_x: int, new_y: int): # moves the current particle
        self.__x = new_x
        self.__y = new_y
        return

    def print_points(self):
        print(self.__x, self.__y)
    
    def get_points(self)->tuple: # gets the points of the current particle
        return self.__x, self.__y
    
    def draw_particle(self, window): # draws the Particle to the window
        py.draw.circle(window, (255, 0, 0), [self.__x, self.__y], self.__radius, 0)
        return

    def set_momentum(self, speed: int, direction: str)->None:
        self.__momentum = (speed, direction)

    def get_momentum(self)->tuple:
        return self.__momentum
