import pyray
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player(Actor):
    """
    A boy with backpack.

    The responsibility of Player is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self, texture='assets/boy.png'):
        super().__init__()
        self._texture = pyray.load_texture(texture)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    # def get_player(self):
    #     return self

    def get_position(self):
        """Gets the actor's position in 2d space.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.

        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

    def draw_player(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        pyray.draw_texture(self._texture, self._position.get_x(),
                           self._position.get_y(), pyray.RAYWHITE)

        # for i in range():
        #     position = Point(x - i * constants.CELL_SIZE, y)
        #     velocity = Point(1 * constants.CELL_SIZE, 0)

        #     player = Actor()
        #     player.set_position(position)
        #     player.set_velocity(velocity)
