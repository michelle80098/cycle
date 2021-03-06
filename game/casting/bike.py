import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Bike(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Bike is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    # TODO add a parameter of color possibly and then have that is called in prepare body to 
    # delinate color Red and Blue
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()
        self._number_of_segments = 1

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        self.grow_tail(1)

    # TODO change to get_bike
    def get_head(self):
        return self._segments[0]

    # TODO change to grow_trail
    def grow_tail(self, number_of_segments):
        for i in range(self._number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.BIKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)