from game.casting.actor import Actor
import math


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self._total_score = 0
        self.add_points(0)
        self.Eternal_score = 0
        print(f'Here is print in SCORE!!!!! {self._points}')

    def add_total_score(self,input):
        '''
        Currently does nothing
        '''
        self._total_score += input
        self.set_text(f"Score: {self.Eternal_score}")
    
    def add_eternal_score(self,input):
        '''
        This keeps track and updates the global score
        '''
        #print(f'OPERATION ETERNAL {self.Eternal_score} += {input}')
        self.Eternal_score += input
        #print(f'OPERATION ETERNAL V2 {self.Eternal_score}')

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self._points = int(math.ceil(self._points))
        self.set_text(f"Score: {self._points}")
        #print(f'Here is add_points print! {self._points}')

    def set_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points = points

    def get_points(self):

        return self._points