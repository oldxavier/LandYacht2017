"""Contains the main entry point of the LandYacht2017 application"""

from queue import Queue
from threading import Thread

from modules.landyacht import landyacht
from modules.skipper import skipper
from modules.ai import ai

def main():
    """Implements the main entry point"""

    # Create the message queues
    command_queue = Queue()
    control_queue = Queue()
    monitor_queue = Queue()

    # Create the threads
    landyacht_thread = Thread(target=landyacht, args=(control_queue, monitor_queue))
    skipper_thread = Thread(target=skipper, args=(command_queue, control_queue, monitor_queue))
    ai_thread = Thread(target=ai, args=(command_queue, control_queue, monitor_queue))

    # Start the threads
    landyacht_thread.start()
    skipper_thread.start()
    ai_thread.start()

    # Join the threads and wait for them to exit
    landyacht_thread.join()
    skipper_thread.join()
    ai_thread.join()

# Define the main entry point
if __name__ == "__main__":
    main()
