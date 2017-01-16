"""Contains the landyacht module"""

from queue import Queue, Empty

from devices.devices import Controller, Servo, RotationSensor, Compass, GPS, Speedometer

from .messages import ControlMessageType, ControlMessage
from .messages import MonitorMessageType, MonitorMessage

from .world import World

def landyacht(control_queue, monitor_queue):
    """Implements the landyacht module"""

    # Create the world
    world = World()

    # Create a controller
    controller = Controller()

    # Create the devices attached to the land yacht
    steering_wheel = Servo(controller, world)
    sail = Servo(controller, world)
    vane = RotationSensor(controller, world)
    compass = Compass(controller, world)
    gps = GPS(controller, world)
    speedometer = Speedometer(controller, world)

    # Create a variable to store the last message
    control_message = ControlMessage(ControlMessageType.CONTINUE_OPERATION)

    # Run until a STOP_LANDYACHT control message is received
    while True:

        # Try to get the next message from the control queue
        try:

            # If there is a new message then get it and store it
            control_message = control_queue.get(block=False)

        # When there is no new message process the last one
        except Empty:

            if control_message.message_type == ControlMessageType.TEST_LANDYACHT:
                # Test the land yacht
                # TODO: implement self-testing
                pass

            elif control_message.message_type == ControlMessageType.GET_LANDYACHT_STATUS:
                # Get the current status of the land yacht
                steering_wheel_angle = steering_wheel.get_angle()
                sail_angle = sail.get_angle()
                wind_direction = vane.get_direction()
                landyacht_direction = compass.get_direction()
                landyacht_position_x = gps.get_position_x()
                landyacht_position_y = gps.get_position_y()
                landyacht_speed = speedometer.get_speed()
                # Create a monitor message and put it into the monitor queue
                monitor_message = MonitorMessage(
                    MonitorMessageType.LANDYACHT_STATUS,
                    steering_wheel_angle=steering_wheel_angle,
                    sail_angle=sail_angle,
                    wind_direction=wind_direction,
                    landyacht_direction=landyacht_direction,
                    landyacht_position_x=landyacht_position_x,
                    landyacht_position_y=landyacht_position_y,
                    landyacht_speed=landyacht_speed)
                monitor_queue.put(monitor_message)
                # Reset the last message
                control_message = ControlMessage(ControlMessageType.CONTINUE_OPERATION)

            elif control_message.message_type == ControlMessageType.TURN_STEERING_WHEEL:
                # Turn the steering wheel by the angle specified
                steering_wheel.turn(control_message.angle)
                # Reset the last message
                control_message = ControlMessage(ControlMessageType.CONTINUE_OPERATION)

            elif control_message.message_type == ControlMessageType.TURN_SAIL:
                # Turn the sail by the angle specified
                sail.turn(int(control_message.angle))
                # Reset the last message
                control_message = ControlMessage(ControlMessageType.CONTINUE_OPERATION)

            elif control_message.message_type == ControlMessageType.STOP_LANDYACHT:
                # Exit the loop and let the thread stop
                break
