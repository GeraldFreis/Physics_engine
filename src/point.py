"""Class to handle the points on the screen in py
attrs:
    x, y --> points controlling the x and y position of this class"""
class Point():
    def __init__(self): # default constructor
        self.x = 0
        self.y = 0
    
    def __init__(self, _x: int, _y: int): # parameterised constructor
        self.x = _x
        self.y = _y
    
    def set_points(self, _x: int, _y: int): # changing the points
        self.x = _x; self.y = _y
    
    def get_points(self):
        return tuple(self.x, self.y)

    def print_points(self):
        print(self.x, self.y)