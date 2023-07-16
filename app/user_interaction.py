import random
import time
from collections import deque
from typing import NoReturn


class UserInteraction:
    """A class to represent the user's interactions with the car."""

    def __init__(self, car) -> None:
        # Initialise the user's commands and preferences as a deque and a dictionary.
        self.user_commands = deque()
        self.user_preferences = {"temperature": 22, "seat_heating": False}

        # Reference to the car instance
        self.car = car

    def get_available_commands(self) -> list[str]:
        """Returns the list of available commands."""

        # The list of commands that user can perform
        return ["set_temperature", "toggle_seat_heating", "set_destination"]

    def set_preference(self, preference, value) -> None:
        """Sets a user preference to a given value."""

        # Update user preferences with new value
        self.user_preferences[preference] = value
        print(f"Preference set: {preference} to {value}")

    def display_status(self, statuses) -> None:
        """Displays a given set of status values."""

        # Iterates over the given statuses and print each of them
        for status, value in statuses.items():
            print(f"{status}: {value}")

    def handle_commands(self) -> NoReturn:
        """Continuously accepts and handles user commands."""

        # Infinite loop to keep accepting commands
        while True:
            # Get the latest command
            command = self.get_command()

            # If command is 'set_destination', calculate a new route
            if command == "set_destination":
                self.car.autonomous_navigation.calculate_route(
                    [random.randint(-100, 100), random.randint(-100, 100)]
                )
            # If command is 'set_temperature', set a new temperature value
            elif command == "set_temperature":
                self.set_preference("temperature", random.randint(18, 28))
            # If command is 'toggle_seat_heating', toggle the seat heating
            elif command == "toggle_seat_heating":
                self.set_preference(
                    "seat_heating", not self.user_preferences["seat_heating"]
                )
            # Wait for 8 seconds before accepting another command
            time.sleep(8)

    def get_command(self) -> str:
        """Returns a user command randomly selected for the demo."""

        # Return a random command from the available commands
        return random.choice(self.get_available_commands())
