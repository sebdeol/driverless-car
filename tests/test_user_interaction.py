from collections import deque
from unittest.mock import MagicMock, patch

from app.user_interaction import UserInteraction


def test_init() -> None:
    car_mock = MagicMock()
    ui = UserInteraction(car_mock)

    assert isinstance(ui.user_commands, deque)
    assert ui.user_preferences == {"temperature": 22, "seat_heating": False}
    assert ui.car == car_mock


def test_get_available_commands() -> None:
    car_mock = MagicMock()
    ui = UserInteraction(car_mock)
    commands = ui.get_available_commands()

    assert set(commands) == {
        "set_temperature",
        "toggle_seat_heating",
        "set_destination",
    }


def test_set_preference() -> None:
    car_mock = MagicMock()
    ui = UserInteraction(car_mock)

    with patch("builtins.print") as mocked_print:
        ui.set_preference("temperature", 24)

    assert ui.user_preferences["temperature"] == 24
    mocked_print.assert_called_once_with("Preference set: temperature to 24")


def test_display_status() -> None:
    car_mock = MagicMock()
    ui = UserInteraction(car_mock)
    statuses = {"speed": 50, "direction": 0}

    with patch("builtins.print") as mocked_print:
        ui.display_status(statuses)

    mocked_print.assert_any_call("speed: 50")
    mocked_print.assert_any_call("direction: 0")


def test_get_command() -> None:
    car_mock = MagicMock()
    ui = UserInteraction(car_mock)

    with patch("random.choice", return_value="set_temperature"):
        command = ui.get_command()

    assert command == "set_temperature"
