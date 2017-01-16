"""Contains the World and related classes"""

import time
import math

# Default values for World and related classes
WORLD_SIZE_X = 0
WORLD_SIZE_Y = 0
WIND_DIRECTION = 0
WIND_SPEED = 0
SHIP_DIRECTION = 45
SHIP_SPEED = 1
SHIP_POSITION_X = 0
SHIP_POSITION_Y = 0
SHIP_STEERING_WHEEL_ANGLE = 0

class World(object):
    """Implements the World class"""

    def __init__(self, world_data_file=None):
        """Instantiates a World"""

        if world_data_file is None:

            # Use default values to configure the world
            self._size_x = int(WORLD_SIZE_X)
            self._size_y = int(WORLD_SIZE_Y)
            self._wind = Wind(int(WIND_DIRECTION), int(WIND_SPEED))
            self._ship = Ship(
                int(SHIP_DIRECTION),
                int(SHIP_SPEED),
                int(SHIP_POSITION_X),
                int(SHIP_POSITION_Y),
                int(SHIP_STEERING_WHEEL_ANGLE))

        else:

            # Load values from a file to configure the world
            # TODO: implement file management
            pass

        # Save the current time for future calculations
        self.current_time = time.time()

    def update(self):
        """Updates the state of the things (basically, ships) in the world"""

        """
        # Display the current state of the world
        print("Current time: {}".format(self.current_time))
        print("Wind direction: {}".format(self._wind.direction))
        print("Landyacht direction: {}".format(self._ship.direction))
        print("Landyacht X position: {}".format(self._ship.position_x))
        print("Landyacht Y position: {}".format(self._ship.position_y))
        print("Landyacht speed: {}".format(self._ship.speed))
        print("Landyacht steering wheel angle: {}".format(self._ship.steering_wheel_angle))
        print()
        """

        # Calculate the elapsed time since the last measurement and save the current time
        new_time = time.time()
        elapsed_time = new_time - self.current_time
        self.current_time = new_time

        # Calculate the new position of the ship based on direction, speed, amd elapsed time
        self._ship.position_x += math.cos(math.radians(self._ship.direction)) * self._ship.speed * elapsed_time
        self._ship.position_y += math.sin(math.radians(self._ship.direction)) * self._ship.speed * elapsed_time

        # Calculate the speed of the ship based on its direction
        # HACK: use the same speed for all wind and land yacht directions so no action needed

        # Calculate the direction of the ship based on the current direction and the steering wheel angle
        self._ship.direction += self._ship.steering_wheel_angle
        if self._ship.direction >= 0:
            self._ship.direction %= 360
        else:
            self._ship.direction %= -360

    def get_wind_direction(self):
        """Returns the direction of the wind"""
        self.update()
        return self._wind.direction

    def get_wind_speed(self):
        """Returns the speed of the wind"""
        self.update()
        return self._wind.speed

    def get_ship_direction(self):
        """Returns the direction of the ship"""
        self.update()
        return self._ship.direction

    def change_ship_direction(self, angle):
        """changes the direction of the ship by the angle specified"""
        self._ship.steering_wheel_angle = angle
        self.update()

    def get_ship_speed(self):
        """Returns the speed of the ship"""
        self.update()
        return self._ship.speed

    def get_ship_position_x(self):
        """Returns the X position of the ship"""
        self.update()
        return self._ship.position_x

    def get_ship_position_y(self):
        """Returns the Y position of the ship"""
        self.update()
        return self._ship.position_y

class Wind(object):
    """Implements the Wind class"""

    def __init__(self, direction, speed):
        """Instantiates a Wind"""
        self.direction = direction
        self.speed = speed

class Ship(object):
    """Implements the Ship class"""

    def __init__(self, direction, speed, position_x, position_y, steering_wheel_angle):
        """Instantiates a Ship"""
        self.direction = direction
        self.speed = speed
        self.position_x = position_x
        self.position_y = position_y
        self.steering_wheel_angle = steering_wheel_angle
