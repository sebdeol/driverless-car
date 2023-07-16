import math
import time

from collections import deque


class AutonomousNavigation:
    """A class to represent the car's autonomous navigation system."""

    def __init__(self, car) -> None:
        self.route = deque()
        self.car = car

    def calculate_route(self, destination) -> None:
        """Calculates the route to a given destination."""

        print("Calculating new route...")
        self.route.append(destination)

    def make_decisions(self) -> None:
        """Continuously makes decisions based on the car's route and sensor data."""

        while True:
            if len(self.route) > 0:
                self.execute_commands()
            time.sleep(1)

    def calculate_direction(self, current_location, next_location):
        """Calculate direction based on current and next location."""

        dx = next_location[0] - current_location[0]
        dy = next_location[1] - current_location[1]

        direction = math.degrees(math.atan2(dy, dx))
        return direction

    def avoid_obstacle(self, obstacle):
        """Adjusts the car's route to avoid a detected obstacle."""

        print(f"Avoiding obstacle at {obstacle['location']}")
        self.car.adjust_steering((self.car.direction + 45) % 360)
        print(f"Car direction adjusted to {self.car.direction}")

    def execute_commands(self) -> None:
        """Executes the next command in the car's route."""

        if len(self.route) > 0:
            next_location = self.route.popleft()
            print(f"Routing to {next_location}")

            direction_to_next = self.calculate_direction(self.car.location, next_location)

            self.car.control_engine(60)
            print("Car speed set to 60")
            self.car.adjust_steering(direction_to_next)
            print(f"Car direction set to {direction_to_next}")

            if self.car.location == next_location:
                print("Destination reached, stopping the car.")
                self.car.apply_brakes()

            time.sleep(1)
