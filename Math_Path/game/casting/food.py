import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Food(Actor):
    """
    Food = Pineapples that are displayed on the screen and some earn points and 1 looses points. 
    
    The responsibility of Food is to select a randomly position either 2 pineapples with varing points to earn or one pineapple that has a negative impact on the players earnings. 

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.reset()

    def food_left(self, texture = 'assets/happypine.png'):
        if random.randint(1,2) == 1:
            self._texture = 'assets/happypine.png'
        else:
            self._texture = 'assets/excitedpine.png'

    def food_right(self, texture = 'assets/happypine.png'):
        if random.randint(1,2) == 1:
            self._texture = 'assets/happypine.png'
        else:
            self._texture = 'assets/excitedpine.png'

    def food_Full_width(self, texture = 'assets/happypine.png'):
        self._texture = 'assets/angrypine.png'

    ### Find out if this is needed still
    def reset(self):
        """Selects a random position and points that the food is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        return self._points   