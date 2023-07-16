import random
import time

from collections import deque
from typing import NoReturn


class UserInteraction:
    """A class to represent the user's interactions with the car."""

    def __init__(self, car) -> None:
        self.user_commands = deque()
        self.user_preferences = {"temperature": 22, "seat_heating": False}
        self.car = car

    def get_available_commands(self) -> list[str]:
        """Returns the list of available commands."""

        return ["set_temperature", "toggle_seat_heating", "set_destination"]

    def set_preference(self, preference, value) -> None:
        """Sets a user preference to a given value."""

        self.user_preferences[preference] = value
        print(f"Preference set: {preference} to {value}")

    def display_status(self, statuses) -> None:
        """Displays a given set of status values."""

        for status, value in statuses.items():
            print(f"{status}: {value}")

    def handle_commands(self) -> NoReturn:
        """Continuously accepts and handles user commands."""

        while True:
            command = self.get_command()
            if command == "set_destination":
                self.car.autonomous_navigation.calculate_route([random.randint(-100, 100), random.randint(-100, 100)])
            elif command == "set_temperature":
                self.set_preference("temperature", random.randint(18, 28))
            elif command == "toggle_seat_heating":
                self.set_preference("seat_heating", not self.user_preferences["seat_heating"])
            time.sleep(10)

    def get_command(self) -> str:
        """Returns a user command randomly selected for the demo."""

        return random.choice(self.get_available_commands())
