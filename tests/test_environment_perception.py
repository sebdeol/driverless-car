from collections import defaultdict
from unittest.mock import MagicMock, patch

from app.environmental_perception import EnvironmentalPerception


def test_init() -> None:
    car_mock = MagicMock()
    env = EnvironmentalPerception(car_mock)

    assert isinstance(env.sensor_data, defaultdict)
    assert env.detected_objects == []
    assert env.car == car_mock


def test_process_data_no_object_detected() -> None:
    car_mock = MagicMock()
    env = EnvironmentalPerception(car_mock)
    data = {"speed": 50, "direction": 0}

    with patch("random.randint", return_value=5):
        env.process_data(data)

    assert env.sensor_data == data
    assert env.detected_objects == []


def test_process_data_object_detected() -> None:
    car_mock = MagicMock()
    env = EnvironmentalPerception(car_mock)
    data = {"speed": 50, "direction": 0}

    with patch("random.randint", return_value=8):
        env.process_data(data)

    assert env.sensor_data == data
    assert len(env.detected_objects) == 1
    assert env.detected_objects[0]["type"] == "Obstacle"
    assert env.detected_objects[0]["location"] in [[i, j] for i in range(-100, 101) for j in range(-100, 101)]
    car_mock.autonomous_navigation.avoid_obstacle.assert_called_once()
