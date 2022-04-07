import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Food(Actor):
    """
    A tasty item that the player likes to eat.
    
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
        self.set_text(str(self._points))
        self.set_color(constants.RED)
        score = cast.get_first_actor("scores")
        
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the food is worth."""
        #print(score._points)
        #print(self._points)

        # self.operation_int = random.randint(1, 6)
        # points = random.randint(1, 100)
        # self._points = points

        # if self.operation_int == 1:
        #     operation = "+ " + str(points)
        #     self.set_color(constants.GREEN)
        #     self._points = self._points * 1

        # elif self.operation_int == 2:
        #     operation = "+ " + str(points)
        #     self.set_color(constants.GREEN)
        #     self._points = self._points * 1

        # elif self.operation_int == 3:
        #     operation = "- " + str(points)
        #     self._points = self._points * -1
        #     self.set_color(constants.RED)

        # elif self.operation_int == 4:
        #     operation = "- " + str(points)
        #     self.set_color(constants.RED)
        #     self._points = self._points * -1
            
        # elif self.operation_int == 5:
        #     operation = "--H A P P Y--" + str(points)
        #     self.set_color(constants.PINK)
        #     self._points = self._points * 1

        # else:
        #     operation = "--D E A T H--" + str(points)
        #     self.set_color(constants.RED)
        #     # self._points = (self._points * -1) * 100  
        #     self._points = self._points * 0

        self._points = random.choice([-5,-10,5,10,20])
        self.set_text(str(self._points))

        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(400, 405)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        return self._points

    def get_points(self):
        """Gets the points the food is worth.
        
        Returns:
            points (int): The points the food is worth.
        """
        
        return self._points

    def calculate_new_score(self, score):
        score = score._points + self._points
        
        # if self.operation_int == 1:
        #     score = score._points + self._points

        #     # score =+ self._points
        #     print(f'Here is what I do! score {score} self._points {self._points} self.operation_int {self.operation_int}')

        # elif self.operation_int == 2:
        #     score = score._points + self._points

        #     # score =+ self._points
        #     print(f'Here is what I do! score {score} self._points {self._points} self.operation_int {self.operation_int}')
        
        # elif self.operation_int == 3:
        #     score = score._points - self._points

        #     # score =- self._points
        #     print(f'Here is what I do! score {score} self._points {self._points} self.operation_int {self.operation_int}')

        # elif self.operation_int == 4:
        #     score = score._points - self._points

        #     # score =- self._points
        #     print(f'Here is what I do! score {score} self._points {self._points} self.operation_int {self.operation_int}')

        # elif self.operation_int == 5:
        #     score = abs(score._points + (self._points * self._points))

        #     # score =+ self._points
        #     print(f'Here is what I do! score {score} self._points {self._points} self.operation_int {self.operation_int}')

        # else:
        #     # score = score._points * 0
        #     score = score._points - self._points

        #     # score =+ self._points
        #     print(f'Here is what I do! score {score} self._points {self._points} self.operation_int {self.operation_int}')



        # return score._points

        