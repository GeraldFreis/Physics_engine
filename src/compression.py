"""
Compression class:
* This class will handle the falling and compression behaviours of the square
"""
class Compression():
    __slots__ = ("__object_array", "__compressed_particles")

    def __init__(self):
        self.__object_array = list()
        self.__compressed_particles = list()
    
    def set_object_array(self, given_array: list):
        self.__object_array = given_array;

    """
    Complexity with this behaviour is that we must incrementally move all components / particles outward
    """
    # function to compress the square
    def compression_behaviour(self, momentum: int, i: int)->list:
        for obj in self.__object_array[i:9-i+1]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]-7, obj.get_points()[1]+momentum)
        
        for obj in self.__object_array[10-i:20+i]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0], obj.get_points()[1]+momentum)

        for obj in self.__object_array[20+i:29-i+1]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]+7, obj.get_points()[1]+momentum)
        return self.__object_array
    
    # function to expand the shape after compression
    def expansion_behaviour(self, momentum: int, i: int)->list:
        for obj in self.__object_array[i+1:9-i]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]+7, obj.get_points()[1]+momentum)
        
        for obj in self.__object_array[10-i:20+i]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0], obj.get_points()[1]+momentum)

        for obj in self.__object_array[20+i:29-i+1]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]-6, obj.get_points()[1]+momentum)

        return self.__object_array
    