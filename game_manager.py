import pygame as py


class Game_manager:
    __run_test = None

    def __init__(self):
        self.__run_test = False

    def __init__(self, run_test: bool):
        self.__run_test = run_test

    def user_input(self):
        for event in py.event.get():  # creating a finish function to close the window
            if event.type == py.QUIT:
                self.__run_test = False
                break

    def get_run_test(self) -> bool:
        return self.__run_test
