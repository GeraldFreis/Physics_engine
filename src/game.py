import pygame as py
from point import Point
from game_manager import Game_manager
from shapes import Shape
from physics_simulations import Physics_Simulations

"""
Class to control the game
    attrs:
        __window_size,
        __background_colour,
        
    methods:
        mainscreen(){handles the window created on the screen
"""
class Game():
    __window_size = None
    __background_colour = None

    def __init__(self):
       self.__window_size = tuple(500, 700)

    def __init__(self, window_size: tuple):
        self.__window_size = window_size
    
    """Function that creates the screen """
    def mainscreen(self):
        # vars
        management = Game_manager(True)
        py.display.init()
        window = py.display.set_mode((self.__window_size))
        py.display.set_caption("Physics Engine - by Gerald Freislich")
        pressed_keys = py.key.get_pressed()

        management.user_input()

        running_test = True
        dropped = False
        mouse_moved = False
        re_run_test = False

        shape = Shape()
        simulation = Physics_Simulations()

        
        while(running_test is True): # while the game is running
            window.fill((0, 0, 0))  # Clear the screen.
            management.user_input()
            mouse_moved = management.get_mouse_move()
            running_test = management.get_run_test()
            re_run_test = management.get_re_run()
            shape.set_drop(management.get_drop_test())

            if(re_run_test is True):
                management.set_drop_test(True)
                management.set_re_run(False)
                simulation.set_stage(0)

            if(shape.get_drop() is False):

                window.fill((0, 0, 0))
                simulation.drop_square(shape.get_shape_array())
                shape.set_shape_array(simulation.get_shape_array())
                # shape.set_drop(True)
                shape.draw_shape(window)

            else:
                shape.make_shape_array_square(mouse_moved, management.get_mouse_pos())
                shape.draw_shape(window)


            py.display.update()
    
    def __del__(self):
        print("Engine ended")

