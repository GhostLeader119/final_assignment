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
        self._stage = True
        self.set_text("+20")
        self.set_color(constants.RED)
        self.reset(1)
        
        
        # NEEDS TO BE CHANGED:
        # - Needs patterned movement
    def reset(self, current_score):
        """Selects a random position and points that the food is worth."""
        operation_int = random.randint(1, 4)
        points = random.randint(1, 100)

        if operation_int == 1:
            operation = "x " + str(points)
            self._points = (current_score * points) - current_score

        elif operation_int == 2:
            operation = "+ " + str(points)
            self._points = (current_score + points) - current_score
        
        elif operation_int == 3:
            operation = "- " + str(points)
            self._points = (current_score - points) - current_score

        else:
            operation = "/ " + str(points)
            self._points = (current_score / points) - current_score
        
        self.set_text(str(operation))

        self._stage = not self._stage
        print(self._stage)

        if self._stage:
            x = 1
            y = int(400)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)
            self.set_position(position)

        else:
            x = constants.CELL_SIZE
            y = int(400)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)
            self.set_position(position)

    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        
        return self._points

        