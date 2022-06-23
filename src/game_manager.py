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
    __slots__ = ("__run_test", "__drop_sim", "__mouse_x", "__mouse_y", "__mouse_moved", "__re_run")

    def __init__(self):
        self.__run_test = False
        self.__drop_sim = True
        self.__mouse_x = 0; self.__mouse_y = 0
        self.__mouse_moved = False
        self.__re_run = False

    def __init__(self, run_test: bool):
        self.__run_test = run_test
        self.__drop_sim = True
        self.__mouse_x = 0; self.__mouse_y = 0
        self.__mouse_moved = False
        self.__re_run = False


    """Getting the user input"""
    def user_input(self):
        pressed_keys = py.key.get_pressed()

        for event in py.event.get():  # creating a finish function to close the window

            if event.type == py.QUIT:
                self.__run_test = False
                break

            if event.type == py.MOUSEMOTION:
                self.__mouse_x, self.__mouse_y = py.mouse.get_pos()
                self.__mouse_moved = True
                break

        if(pressed_keys[py.K_1]):
            self.__drop_sim = False
            print("Here")
        
        if(pressed_keys[py.K_2]):
            self.__re_run = True

            
    
    # returns the run test _value (if the user has decided to exit the game) and the 
    def get_run_test(self) -> bool:
        return self.__run_test
    
    def get_drop_test(self) -> bool:
        return self.__drop_sim

    def set_drop_test(self, droptest: bool) -> None: self.__drop_sim = droptest

    def get_mouse_move(self)->bool: 
        return self.__mouse_moved

    def get_mouse_pos(self)->tuple: 
        return (self.__mouse_x, self.__mouse_y)
    
    def get_re_run(self)->bool: return self.__re_run

    def set_re_run(self, rerun: bool)->None: self.__re_run = rerun


