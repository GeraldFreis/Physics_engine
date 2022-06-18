import pygame as py

"""
Class to manage the game (specifically inputs):
    has private attrs:
        __run_test (bool to check whether or not to end the game)
        __drop_sim (bool to check if the user has pressed 1 (and if so we can begin dropping the square))
    
    has public functions:
        user_input() # checks what the user has entered (i.e to end (has clicked quit))

        get run_tests, get drop_tests # returns the private variables in each of the functions
"""
class Game_manager:
    __run_test = None
    __drop_sim = None

    def __init__(self):
        self.__run_test = False
        self.__drop_sim = True

    def __init__(self, run_test: bool):
        self.__run_test = run_test
        self.__drop_sim = True

    """Getting the user input"""
    def user_input(self):
        pressed_keys = py.key.get_pressed()
        for event in py.event.get():  # creating a finish function to close the window
            if event.type == py.QUIT:
                self.__run_test = False
                break
        if(pressed_keys[py.K_1]):
            self.__drop_sim = False
            
    
    # returns the run test _value (if the user has decided to exit the game) and the 
    def get_run_test(self) -> bool:
        return self.__run_test
    
    def get_drop_test(self) -> bool:
        return self.__drop_sim
