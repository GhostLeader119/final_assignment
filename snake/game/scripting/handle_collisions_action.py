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

    
class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_game_over(cast)
            # self._handle_zone_collision(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        food = cast.get_first_actor("foods")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()
    
        if head.get_position().equals(food.get_position()):
            
            # snake.grow_tail(points)
            current_score = score.get_points()
            
            food.reset(current_score)

            points = food.get_points()
            score.add_points(points)
            
            print(777)

    # def _handle_zone_collision(self,cast):
    #     '''
    #     Checks to see if the player avatar is located in the two end zones to end the round.

    #     Inputs:
    #     Cast should be the X value of the players location.
    #     Outputs:
    #     Returns a 1 for if the player is in zone 1 or 2 if player is in zone 2

    #     Zone 1  |  Zone 2
    #             |
    #             |
    #             |
    #             |

    #     '''
        
    #     zone_1_max_x = constants.ZONE_1_MAX_X
    #     zone_1_min_x = constants.ZONE_1_MIN_X
    #     zone_2_max_x = constants.ZONE_2_MAX_X
    #     zone_2_min_x = constants.ZONE_2_MIN_X


    #     if cast >= zone_1_min_x and cast <= zone_1_max_x:

    #         return 1
    #     elif cast >= zone_2_min_x and cast <= zone_2_max_x:

    #         return 2


    
        
    # CLEANUP ACCORDINGLY
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)