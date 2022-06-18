from point import Point # class that creates points
import pygame as py
from game import  Game

if __name__ == "__main__":
    point_1 = Point(0, 2) # first point

    game_interface = Game((700,500))
    game_interface.mainscreen()
