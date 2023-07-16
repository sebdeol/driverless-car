import random
from collections import defaultdict


class EnvironmentalPerception:
    """A class to represent the car's environmental perception system."""

    def __init__(self, car) -> None:
        # Initialise the sensor data dictionary and the detected objects list
        self.sensor_data = defaultdict(int)
        self.detected_objects = []

        # Store a reference to the car instance
        self.car = car

    def process_data(self, data) -> None:
        """Processes and updates the car's sensor data, detecting objects if necessary."""

        # Update the sensor data with the new data
        self.sensor_data.update(data)

        # Randomly simulate the detection of an object
        if random.randint(0, 10) > 7:
            # Create a detected object
            detected_object = {
                "type": "Obstacle",
                "location": [random.randint(-100, 100), random.randint(-100, 100)],
            }

            # Add the detected object to the list
            self.detected_objects.append(detected_object)
            print(f"Object detected: {detected_object}")

            # Tell the car's autonomous navigation system to avoid the obstacle
            self.car.autonomous_navigation.avoid_obstacle(detected_object)
