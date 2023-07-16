import random

from collections import defaultdict


class EnvironmentalPerception:
    """A class to represent the car's environmental perception system."""

    def __init__(self, car) -> None:
        self.sensor_data = defaultdict(int)
        self.detected_objects = []
        self.car = car

    def process_data(self, data) -> None:
        """Processes and updates the car's sensor data, detecting objects if necessary."""

        self.sensor_data.update(data)
        if random.randint(0, 10) > 7:
            detected_object = {
                "type": "Obstacle",
                "location": [random.randint(-100, 100), random.randint(-100, 100)],
            }
            self.detected_objects.append(detected_object)
            print(f"Object detected: {detected_object}")
            self.car.autonomous_navigation.avoid_obstacle(detected_object)
