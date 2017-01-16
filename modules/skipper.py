"""Contains the skipper module"""

from enum import Enum, auto

from .messages import CommandMessageType, CommandMessage
from .messages import ControlMessageType, ControlMessage

def skipper(command_queue, control_queue, monitor_queue):
    """Implements the skipper module"""

    # Display help
    display_help()

    # Wait for user input
    while True:

        # Ask for the user's selection
        choice = int(input("Enter the number of operation you selected: "))

        # Process the user's selection
        if choice == Operation.DISPLAY_HELP.value:
            # Display help
            display_help()

        elif choice == Operation.GET_LANDYACHT_STATUS.value:
            # Get the overall status of the land yacht
            # Create and send a GET_LANDYACHT_STATUS message to tle land yacht
            control_message = ControlMessage(ControlMessageType.GET_LANDYACHT_STATUS)
            control_queue.put(control_message)
            # Wait from the requested data from the land yacht
            monitor_message = monitor_queue.get()
            # Display the data
            print("Steering wheel angle: {} degrees".format(monitor_message.steering_wheel_angle))
            print("Sail angle: {} degrees".format(monitor_message.sail_angle))
            print("Wind direction: {} degrees".format(monitor_message.wind_direction))
            print("Land yacht direction: {} degrees".format(monitor_message.landyacht_direction))
            print("Land yacht X position: {}".format(monitor_message.landyacht_position_x))
            print("Land yacht Y position: {}".format(monitor_message.landyacht_position_y))
            print("Land yacht speed: {}".format(monitor_message.landyacht_speed))

        elif choice == Operation.TURN_STEERING_WHEEL.value:
            # Turn the steering wheel by the angle specified by the user
            angle = int(input("Enter the new angle for the steering wheel: "))
            # Create and send a TURN_STEERING_WHEEL message to the land yacht
            control_message = ControlMessage(ControlMessageType.TURN_STEERING_WHEEL, angle=angle)
            control_queue.put(control_message)

        elif choice == Operation.TURN_SAIL.value:
            # Turn the sail by the angle specified by the user
            angle = int(input("Enter the new angle for the sail: "))
            # Create and send a TURN_SAIL message to the land yacht
            control_message = ControlMessage(ControlMessageType.TURN_SAIL, angle=angle)
            control_queue.put(control_message)

        elif choice == Operation.NAVIGATE_TO_DIRECTION.value:
            # Navigate to the direction specified by the user
            direction = int(input("Enter the direction of the navigation target: "))
            # Create and send a NAVIGATE_TO_DIRECTION message to the AI
            command_message = CommandMessage(CommandMessageType.NAVIGATE_TO_DIRECTION, direction=direction)
            command_queue.put(command_message)

        elif choice == Operation.NAVIGATE_TO_POSITION.value:
            # Navigate to the position specified by the user
            position_x = int(input("Enter the X position of the navigation target: "))
            position_y = int(input("Enter the Y position of the navigation target: "))
            # Create and send a NAVIGATE_TO_POSITION message to the AI
            command_message = CommandMessage(CommandMessageType.NAVIGATE_TO_POSITION, position_x=position_x, position_y=position_y)
            command_queue.put(command_message)

        elif choice == Operation.STOP_LANDYACHT.value:
            # Stop the land yacht
            # Create and send a STOP_AI message to the AI
            command_message = CommandMessage(CommandMessageType.STOP_AI)
            command_queue.put(command_message)
            # Create and send a STOP_LANDYACHT message to the land yacht
            control_message = ControlMessage(ControlMessageType.STOP_LANDYACHT)
            control_queue.put(control_message)
            # Exit the loop and let the thread stop
            break

        else:
            # Notify the user that there is no such command and display help
            print("There is no such command.")
            display_help()

def display_help():
    """Displays the list of available operations"""
    print("Operations:")
    print("{} - Display help".format(Operation.DISPLAY_HELP.value))
    print("{} - Get the status of the land yacht".format(Operation.GET_LANDYACHT_STATUS.value))
    print("{} - Turn the steering wheel".format(Operation.TURN_STEERING_WHEEL.value))
    print("{} - Turn the sail".format(Operation.TURN_SAIL.value))
    print("{} - Navigate to direction".format(Operation.NAVIGATE_TO_DIRECTION.value))
    print("{} - Navigate to position".format(Operation.NAVIGATE_TO_POSITION.value))
    print("{} - Stop the land yacht".format(Operation.STOP_LANDYACHT.value))

class Operation(Enum):
    """Implements the Operation enumeration"""
    DISPLAY_HELP = 0
    GET_LANDYACHT_STATUS = auto()
    TURN_STEERING_WHEEL = auto()
    TURN_SAIL = auto()
    NAVIGATE_TO_DIRECTION = auto()
    NAVIGATE_TO_POSITION = auto()
    STOP_LANDYACHT = 9
