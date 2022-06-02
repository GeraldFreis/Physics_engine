import pygame as py


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
