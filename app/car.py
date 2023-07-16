import random
import time
from threading import Thread
from typing import NoReturn

from app.autonomous_navigation import AutonomousNavigation
from app.environmental_perception import EnvironmentalPerception
from app.user_interaction import UserInteraction


class Car:
    """A class to represent the autonomous car."""

    def __init__(self) -> None:
        # Initialise the car's speed, direction, and location
        self.speed = 0
        self.direction = 0
        self.location = [0, 0]

        # Initialise the car's sensors
        self.sensors = {
            "speed": self.speed,
            "direction": self.direction,
            "location": self.location,
        }

        # Initialise the car's sub-systems
        self.autonomous_navigation = AutonomousNavigation(self)
        self.environmental_perception = EnvironmentalPerception(self)
        self.user_interaction = UserInteraction(self)

    def control_engine(self, speed) -> None:
        """Controls the car's engine, setting its speed."""

        # Set the car's speed
        self.speed = speed
        print(f"Engine controlled to set speed to {speed}")

    def adjust_steering(self, direction) -> None:
        """Adjusts the car's steering, changing its direction."""

        # Set the car's direction
        self.direction = direction
        print(f"Steering adjusted to direction {direction}")

    def apply_brakes(self) -> None:
        """Applies the car's brakes, stopping it."""

        # Stop the car
        self.speed = 0
        print("Brakes applied")

    def handle_sensors(self) -> NoReturn:
        """Checks and updates the car's sensor data continuously."""

        # Infinite loop to keep checking and updating the sensors
        while True:
            # Retrieve the latest sensor data
            data = self.retrieve_sensor_data()

            # Update the car's sensor data
            self.sensors.update(data)

            # Process the sensor data
            self.environmental_perception.process_data(self.sensors)

            # Pause for a second before the next loop iteration
            time.sleep(1)

    def retrieve_sensor_data(self) -> dict[str, int | list[int]]:
        """Retrieves and returns the car's sensor data."""

        # Simulate changes in speed and direction
        self.speed += random.randint(-5, 5)
        self.direction += random.randint(-10, 10)

        # Calculate the new location based on the current speed and direction
        new_location = self.location[:]
        new_location[0] += self.speed * 0.5 * (1 if self.direction >= 0 else -1)
        new_location[1] += self.speed * 0.5 * (1 if self.direction < 0 else -1)
        self.location = new_location

        # Create a dictionary of the sensor data
        data = {
            "speed": self.speed,
            "direction": self.direction,
            "location": self.location,
        }

        # Update the car's sensor data
        self.sensors.update(data)

        return data


if __name__ == "__main__":
    # Create a Car instance
    car = Car()

    # Calculate a random route for the car
    car.autonomous_navigation.calculate_route(
        [random.randint(-100, 100), random.randint(-100, 100)]
    )

    try:
        # Create threads to handle the sensors, make decisions, and handle the user interactions commands.
        sensor_thread = Thread(target=car.handle_sensors)
        decision_thread = Thread(target=car.autonomous_navigation.make_decisions)
        commands_thread = Thread(target=car.user_interaction.handle_commands)

        # Start the threads
        sensor_thread.start()
        decision_thread.start()
        commands_thread.start()
    except KeyboardInterrupt:
        # If a keyboard interrupt is detected, end the program
        pass
