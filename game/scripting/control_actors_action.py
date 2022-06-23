from game import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_p1 = Point(constants.CELL_SIZE, 0)
        self._direction_p2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snake_p1 = cast.get_actors("snakes")[0]
        snake_p2 = cast.get_actors("snakes")[1]
        # left p1
        if self._keyboard_service.is_key_down('a'):
            self._direction_p1 = Point(-constants.CELL_SIZE, 0)
            color = snake_p1.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p1.grow_tail(constants.GROWTH_RATE, color)

        # right p1
        if self._keyboard_service.is_key_down('d'):
            self._direction_p1 = Point(constants.CELL_SIZE, 0)
            color = snake_p1.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p1.grow_tail(constants.GROWTH_RATE, color)


        # up p1
        if self._keyboard_service.is_key_down('w'):
            self._direction_p1 = Point(0, -constants.CELL_SIZE)
            color = snake_p1.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p1.grow_tail(constants.GROWTH_RATE, color)

        # down p1
        if self._keyboard_service.is_key_down('s'):
            self._direction_p1 = Point(0, constants.CELL_SIZE)
            color = snake_p1.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p1.grow_tail(constants.GROWTH_RATE, color)

        # left p2
        if self._keyboard_service.is_key_down('j'):
            self._direction_p2 = Point(-constants.CELL_SIZE, 0)
            color = snake_p2.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p2.grow_tail(constants.GROWTH_RATE, color)


        # right p2
        if self._keyboard_service.is_key_down('l'):
            self._direction_p2 = Point(constants.CELL_SIZE, 0)
            color = snake_p2.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p2.grow_tail(constants.GROWTH_RATE, color)

        # up p2
        if self._keyboard_service.is_key_down('i'):
            self._direction_p2 = Point(0, -constants.CELL_SIZE)
            color = snake_p2.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p2.grow_tail(constants.GROWTH_RATE, color)

        # down p2
        if self._keyboard_service.is_key_down('k'):
            self._direction_p2 = Point(0, constants.CELL_SIZE)
            color = snake_p2.get_segments()[-1].get_color()
            if color != constants.WHITE:
                snake_p2.grow_tail(constants.GROWTH_RATE, color)

        # p1 control
        snake_p1 = cast.get_actors("snakes")[0]
        snake_p1.turn_head(self._direction_p1)

        # p2 control
        snake_p2 = cast.get_actors("snakes")[1]
        snake_p2.turn_head(self._direction_p2)
