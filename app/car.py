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
        self.speed = 0
        self.direction = 0
        self.location = [0, 0]
        self.sensors = {
            "speed": self.speed,
            "direction": self.direction,
            "location": self.location,
        }
        self.autonomous_navigation = AutonomousNavigation(self)
        self.environmental_perception = EnvironmentalPerception(self)
        self.user_interaction = UserInteraction(self)

    def control_engine(self, speed) -> None:
        """Controls the car's engine, setting its speed."""

        self.speed = speed
        print(f"Engine controlled to set speed to {speed}")

    def adjust_steering(self, direction) -> None:
        """Adjusts the car's steering, changing its direction."""

        self.direction = direction
        print(f"Steering adjusted to direction {direction}")

    def apply_brakes(self) -> None:
        """Applies the car's brakes, stopping it."""

        self.speed = 0
        print("Brakes applied")

    def handle_sensors(self) -> NoReturn:
        """Checks and updates the car's sensor data continuously."""

        while True:
            data = self.retrieve_sensor_data()
            self.sensors.update(data)
            self.environmental_perception.process_data(self.sensors)
            time.sleep(1)

    def retrieve_sensor_data(self) -> dict[str, int | list[int]]:
        """Retrieves and returns the car's sensor data."""

        self.speed += random.randint(-5, 5)
        self.direction += random.randint(-10, 10)
        new_location = self.location[:]
        new_location[0] += self.speed * 0.5 * (1 if self.direction >= 0 else -1)
        new_location[1] += self.speed * 0.5 * (1 if self.direction < 0 else -1)
        self.location = new_location

        data = {
            "speed": self.speed,
            "direction": self.direction,
            "location": self.location,
        }

        self.sensors.update(data)

        return data


if __name__ == "__main__":
    car = Car()

    car.autonomous_navigation.calculate_route([random.randint(-100, 100), random.randint(-100, 100)])

    try:
        sensor_thread = Thread(target=car.handle_sensors)
        decision_thread = Thread(target=car.autonomous_navigation.make_decisions)
        commands_thread = Thread(target=car.user_interaction.handle_commands)

        sensor_thread.start()
        decision_thread.start()
        commands_thread.start()
    except KeyboardInterrupt:
        pass
