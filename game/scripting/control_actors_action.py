import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cast import Cast


class ControlActorsAction(Action):
    """
    An input action that controls the Bikes.
    
    The responsibility of ControlActorsAction is to get the direction and move the Bike's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_1 = Point(constants.CELL_SIZE, 0)
        self._direction_2 = Point(constants.CELL_SIZE, 0)
        self.bikes = []

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # print('\n\n\n\n', cast, '\n\n\n\n')

        self.bikes.append(cast.get_actors('bike_1'))
        self.bikes.append(cast.get_actors('bike_2'))
        for bike in self.bikes:
            if cast.get_actors('bike_1') == bike:
                self._bike_1(cast)
            else:
                self._bike_2(cast)
                print('this is firing')

    def _bike_1(self, cast):
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

                
        bike = cast.get_first_actor('bike_1')
        bike.turn_head(self._direction_1)

    
    def _bike_2(self, cast):
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
                
            bike = cast.get_first_actor('bike_2')
            bike.turn_head(self._direction_2)
