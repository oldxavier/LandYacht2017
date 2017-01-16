"""Contains the ai module"""

from queue import Queue, Empty

from .messages import CommandMessageType, CommandMessage
from .messages import ControlMessageType, ControlMessage

def ai(command_queue, control_queue, monitor_queue):
    """Implements the ai module"""

    # Create a variable to store the last message
    command_message = CommandMessage(CommandMessageType.CONTINUE_COURSE)

    # Run until a STOP_AI command message is received
    while True:

        # Try to get the next message from the command queue
        try:

            # If there is a new message then get it and store it
            command_message = command_queue.get(block=False)

        # When there is no new message process the last one
        except Empty:

            if command_message.message_type == CommandMessageType.TEST_AI:
                # Test the AI
                # TODO: implement self-testing
                pass

            elif command_message.message_type == CommandMessageType.NAVIGATE_TO_DIRECTION:
                # Navigate to the direction specified
                # Store the requested direction
                target_direction = command_message.direction
                # Get the current status of the land yacht
                control_message = ControlMessage(ControlMessageType.GET_LANDYACHT_STATUS)
                control_queue.put(control_message)
                monitor_message = monitor_queue.get()
                # Compute the required direction change
                current_direction = monitor_message.landyacht_direction
                angle = target_direction - current_direction
                if angle > 360:
                    angle %= 360
                elif angle < -360:
                    angle %= -360
                # Send the direction change to the land yacht
                message = ControlMessage(ControlMessageType.TURN_STEERING_WHEEL, angle)
                control_queue.put(message)

            elif command_message.message_type == CommandMessageType.NAVIGATE_TO_POSITION:
                # TODO: implement navigation to position
                pass

            elif command_message.message_type == CommandMessageType.STOP_AI:
                # Exit the loop and let the thread stop
                break
