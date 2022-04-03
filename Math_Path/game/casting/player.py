import pyray
from game.casting.actor import Actor


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

    def get_player(self):
        return self

    def draw_player(self):

        pyray.draw_texture(self._texture, self._position.get_x(),
                           self._position.get_y(), pyray.RAYWHITE)
