try:
    import constants
except ModuleNotFoundError:
    print('Error: Could not import [constants] in [handle_collisions_action.py]')
try:
    from game.casting.actor import Actor
except ModuleNotFoundError:
    print('Error: Could not import [Actor] in [handle_collisions_action.py]')
try:
    from game.scripting.action import Action
except ModuleNotFoundError:
    print('Error: Could not import [Action] in [handle_collisions_action.py]')
try:
    from game.shared.point import Point
except ModuleNotFoundError:
    print('Error: Could not import [Point] in [handle_collisions_action.py]')

    
class StageAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    def __init__(self):
        self._stage_1 = True

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_stage(cast)

    def _handle_stage(self, cast):

        if self._stage_1 == True:

            self._start_stage_1(cast)

        else:
            self._start_stage_2(cast)

    def _start_stage_1(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()

    def _start_stage_2(self,cast):
        '''
        Checks to see if the player avatar is located in the two end zones to end the round.

        Inputs:
        Cast should be the X value of the players location.
        Outputs:
        Returns a 1 for if the player is in zone 1 or 2 if player is in zone 2

        Zone 1  |  Zone 2
                |
                |
                |
                |

        '''
        zone_1_max_x = constants.ZONE_1_MAX_X
        zone_1_min_x = constants.ZONE_1_MIN_X
        zone_2_max_x = constants.ZONE_2_MAX_X
        zone_2_min_x = constants.ZONE_2_MIN_X


        if cast >= zone_1_min_x and cast <= zone_1_max_x:

            return 1
        elif cast >= zone_2_min_x and cast <= zone_2_max_x:

            return 2