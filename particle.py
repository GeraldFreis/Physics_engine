import pygame as py


class Particle():
    __radius = None
    __x = None
    __y = None

    # constructors
    def __init__(self):
        self.__radius = 0
    
    def __init__(self, radius: int, x: int, y: int):
        self.__radius = radius
        self.__x = x
        self.__y = y

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
