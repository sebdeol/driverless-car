import math
import time
from collections import deque


class AutonomousNavigation:
    """A class to represent the car's autonomous navigation system."""

    def __init__(self, car) -> None:
        # Initialise the route as a deque
        self.route = deque()

        # Reference to the car instance
        self.car = car

    def calculate_route(self, destination) -> None:
        """Calculates the route to a given destination."""

        print("Calculating new route...")

        # Append the destination to the route
        self.route.append(destination)

    def make_decisions(self) -> None:
        """Continuously makes decisions based on the car's route and sensor data."""

        # Infinite loop to keep making decisions
        while True:
            # Check if there commands to execute
            if len(self.route) > 0:
                # Execute the commands
                self.execute_commands()
            # Wait for a second before the next loop iteration
            time.sleep(1)

    def calculate_direction(self, current_location, next_location):
        """Calculate direction based on current and next location."""

        # Calculate the difference between the current and next location
        dx = next_location[0] - current_location[0]
        dy = next_location[1] - current_location[1]

        # Calculate the direction
        direction = math.degrees(math.atan2(dy, dx))
        return direction

    def avoid_obstacle(self, obstacle):
        """Adjusts the car's route to avoid a detected obstacle."""

        print(f"Avoiding obstacle at {obstacle['location']}")

        # Adjust the steering by 45 degrees to avoid the obstacle
        self.car.adjust_steering((self.car.direction + 45) % 360)
        print(f"Car direction adjusted to {self.car.direction}")

    def execute_commands(self) -> None:
        """Executes the next command in the car's route."""

        # Check if there are commands to execute
        if len(self.route) > 0:
            # Get the next location from the route
            next_location = self.route.popleft()
            print(f"Routing to {next_location}")

            # Calculate the direction to the next location
            direction_to_next = self.calculate_direction(
                self.car.location, next_location
            )

            # Control the car engine and set the speed to 60
            self.car.control_engine(60)
            print("Car speed set to 60")

            # Adjust the steering of the car to the direction to the next location
            self.car.adjust_steering(direction_to_next)
            print(f"Car direction set to {direction_to_next}")

            # Handle if the car has reached the final destination
            if self.car.location == next_location:
                print("Destination reached, stopping the car.")
                # Apply brakes to stop the car
                self.car.apply_brakes()

            # Wait for a second before the next loop iteration
            time.sleep(1)
