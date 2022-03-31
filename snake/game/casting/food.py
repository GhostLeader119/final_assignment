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
    def __init__(self, cast):
        "Constructs a new Food."
        super().__init__()
        self._points = 0
        self.operation_int = 1
        self._stage = True
        self.set_text("+20")
        self.set_color(constants.RED)
        score = cast.get_first_actor("scores")
        
        self.reset(score)
        
        
        # NEEDS TO BE CHANGED:
        # - Needs patterned movement
    def reset(self, score):
        """Selects a random position and points that the food is worth."""
        print(score._points)
        print(self._points)
        # if self.operation_int == 1:
        #     score._points = score._points + self._points

        # elif self.operation_int == 2:
        #     score._points = score._points * self._points
        
        # elif self.operation_int == 3:
        #     score._points = score._points - self._points

        # else:
        #     score._points = score._points - self._points


        self.operation_int = random.randint(1, 4)
        points = random.randint(1, 100)
        self._points = points

        if self.operation_int == 1:
            operation = "+ " + str(points)
            self.set_color(constants.GREEN)

        elif self.operation_int == 2:
            operation = "x " + str(points)
            self.set_color(constants.GREEN)
        
        elif self.operation_int == 3:
            operation = "- " + str(points)
            self.set_color(constants.RED)

        else:
            operation = "- " + str(points)
            self.set_color(constants.RED)
        
        self.set_text(str(operation))

        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(400, 405)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        # self._stage = not self._stage

        # if self._stage:
        #     x = 1
        #     y = int(400)
        #     position = Point(x, y)
        #     position = position.scale(constants.CELL_SIZE)
        #     self.set_position(position)

        # else:
        #     x = constants.CELL_SIZE
        #     y = int(400)
        #     position = Point(x, y)
        #     position = position.scale(constants.CELL_SIZE)
        #     self.set_position(position)

    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        
        return self._points

    def calculate_new_score(self, score):
        
        if self.operation_int == 1:
            score._points = score._points + self._points

        elif self.operation_int == 2:
            score._points = score._points * self._points
        
        elif self.operation_int == 3:
            score._points = score._points - self._points

        else:
            score._points = score._points - self._points

        