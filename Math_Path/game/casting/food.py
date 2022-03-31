import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Food(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        # DO WE NEED THESE
        # self.set_text("@")
        # self.set_color(constants.RED)
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

        
    # NEEDS TO BE CHANGED:
    # - Needs patterned movement
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