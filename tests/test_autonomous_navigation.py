import time

from unittest.mock import patch

from app.autonomous_navigation import AutonomousNavigation
from app.car import Car


def test_calculate_route(car) -> None:
    nav = AutonomousNavigation(car)
    destination = [10, 10]

    assert len(nav.route) == 0
    nav.calculate_route(destination)

    assert len(nav.route) == 1
    assert nav.route[0] == destination


def test_calculate_direction(car) -> None:
    nav = AutonomousNavigation(car)

    current_location = [0, 0]
    next_location = [10, 10]
    expected_direction = 45.0

    calculated_direction = nav.calculate_direction(current_location, next_location)
    assert calculated_direction == expected_direction


def test_avoid_obstacle(car) -> None:
    nav = AutonomousNavigation(car)

    obstacle = {"location": [5, 5]}
    initial_direction = car.direction

    with patch.object(Car, "adjust_steering", return_value=None) as mock:
        nav.avoid_obstacle(obstacle)
        mock.assert_called_once_with((initial_direction + 45) % 360)


def test_execute_commands_no_route(car) -> None:
    nav = AutonomousNavigation(car)

    with patch.object(Car, "control_engine", return_value=None) as mock_engine:
        with patch.object(Car, "adjust_steering", return_value=None) as mock_steering:
            nav.execute_commands()
            mock_engine.assert_not_called()
            mock_steering.assert_not_called()


def test_execute_commands_with_route(car) -> None:
    nav = AutonomousNavigation(car)
    nav.route.append([10, 10])

    with patch.object(time, "sleep"):
        with patch.object(Car, "control_engine", return_value=None) as mock_engine:
            with patch.object(Car, "adjust_steering", return_value=None) as mock_steering:
                with patch.object(AutonomousNavigation, "calculate_direction", return_value=45) as mock_direction:
                    nav.execute_commands()
                    mock_engine.assert_called_once_with(60)
                    mock_steering.assert_called_once_with(45)
                    mock_direction.assert_called_once()
