"""Contains generic device classes"""

SERVO_CENTER = 0
SERVO_MIN_ANGLE = -90
SERVO_MAX_ANGLE = 90

class Controller(object):
    """Implements the Controller class"""

    def __init__(self, controller_type=None, hardware=None):
        """Instantiates a Controller"""
        self.controller_type = controller_type
        self.hardware = hardware

class Servo(object):
    """Implements the Servo class"""

    def __init__(
            self,
            controller,
            world=None,
            pin=None,
            angle=SERVO_CENTER,
            min_angle=SERVO_MIN_ANGLE,
            max_angle=SERVO_MAX_ANGLE):
        """Instantiates a Servo"""
        self.world = world
        self.controller = controller
        self.pin = pin
        self.angle = angle
        self.min_angle = min_angle
        self.max_angle = max_angle

    def get_angle(self):
        """Returns the current angle of the servo"""
        return self.angle

    def turn(self, angle):
        """Turns the servo by the angle specified"""

        # Make sure the angle is between the minimum and maximum angles
        angle = int(angle)
        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle

        # Set the current angle
        self.angle = angle
        self.world.change_ship_direction(angle)

class RotationSensor(object):
    """Implements the RotationSensor class"""

    def __init__(self, controller, world=None, pin=None):
        """Instantiates a RotationSensor"""
        self.controller = controller
        self.world = world
        self.pin = pin

    def get_direction(self):
        """Returns the current direction of the sensor"""
        relative_wind_direction = self.world.get_ship_direction() - self.world.get_wind_direction()
        if relative_wind_direction < 0:
            relative_wind_direction %= -360
        else:
            relative_wind_direction %= 360
        return relative_wind_direction

class Compass(object):
    """Implements the Compass class"""

    def __init__(self, controller, world=None, pin=None):
        """Instantiates a Compass"""
        self.controller = controller
        self.world = world
        self.pin = pin

    def get_direction(self):
        """Returns the current direction of the compass"""
        return self.world.get_ship_direction()

class GPS(object):
    """Implements the GPS class"""

    def __init__(self, controller, world=None, pin=None):
        """Instantiates a GPS"""
        self.controller = controller
        self.world = world
        self.pin = pin

    def get_position_x(self):
        """Returns the X coordinate of the current position"""
        return self.world.get_ship_position_x()

    def get_position_y(self):
        """Returns the Y coordinate of the current position"""
        return self.world.get_ship_position_y()

class Speedometer(object):
    """Implements the Speedometer class"""

    def __init__(self, controller, world=None, pin=None):
        """Instantiates a Speedometer"""
        self.controller = controller
        self.world = world
        self.pin = pin

    def get_speed(self):
        """Returns the speed of the land yacht"""
        return self.world.get_ship_speed()
