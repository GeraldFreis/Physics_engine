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
    def compression_behaviour(self, momentum: int, i: int):
        for obj in self.__object_array[i+1:9-i+1]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]-7, obj.get_points()[1]+momentum)
        
        for obj in self.__object_array[10-i:20+i]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0], obj.get_points()[1]+momentum)

        for obj in self.__object_array[20+i+1:29-i+1]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]+7, obj.get_points()[1]+momentum)
        return self.__object_array
    
    # function to expand the shape after compression
    def expansion_behaviour(self, momentum: int, i: int):
        for obj in self.__object_array[i+1:9-i]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]+7, obj.get_points()[1]+momentum)
        
        for obj in self.__object_array[10-i:20+i]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0], obj.get_points()[1]+momentum)

        for obj in self.__object_array[20+i+1:29-i+1]: # problem (for every iteration we move left and down)
            obj.move_particle(obj.get_points()[0]-7, obj.get_points()[1]+momentum)
        return self.__object_array
    


"""
Plan:
How to move the particles incrementally outwards and down
(We can use indexing, i.e take particles 1->9 and 21->30 and slowly move them outwards):
-> Use case:
    - The bottom of the shape hits 450:
    - The top continues to move down as the sides press out
    - For every iteration the remaining particles move outwards:
        - Remaining means those that are greater than the last particle indexes added to the index list of particles moved
    - We will stop this when there are 4 particles left:
    - for instance, the particles on the left of the shape will move out:
        - index 1 and 9 will join the bottom and top line of the shape respectively
        - index 2 and 8 will again join the bottom and top of the shape for the second iteration
        - index 3 and 7 will join the bottom and top and then we reverse
        - index 3 and 7 will return back to the side, as the top moves up
        - index 2 and 8 will join the side again,
        - index 1 and 9 will join the shape once more
- We will use an index array to keep track of which particles

"""
