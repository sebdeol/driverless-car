import pytest


def test_init(car) -> None:
    assert car.speed == 0
    assert car.direction == 0
    assert car.location == [0, 0]

    assert car.sensors == {
        "speed": car.speed,
        "direction": car.direction,
        "location": car.location,
    }


def test_control_engine(car) -> None:
    assert car.speed == 0

    car.control_engine(50)
    assert car.speed == 50

    car.control_engine(30)
    assert car.speed == 30


@pytest.mark.parametrize("steering_value", (90, -90, 40, 0))
def test_adjust_steering(car, steering_value) -> None:
    car.adjust_steering(steering_value)
    assert car.direction == steering_value


def test_apply_brakes(car) -> None:
    car.control_engine(50)
    assert car.speed == 50

    car.apply_brakes()
    assert car.speed == 0


def test_retrieve_sensor_data(car) -> None:
    data = car.retrieve_sensor_data()

    assert isinstance(data, dict)
    assert set(data.keys()) == {"speed", "direction", "location"}
    assert isinstance(data.get("speed"), int)
    assert isinstance(data.get("direction"), int)
    assert isinstance(data.get("location"), list)


def test_retrieve_sensor_data_upadates_the_sensors_object(car) -> None:
    initial_sensors = car.sensors.copy()
    updated_sensors = car.retrieve_sensor_data()

    assert car.sensors != initial_sensors
    assert car.sensors == updated_sensors
    assert car.sensors == {
        "speed": car.speed,
        "direction": car.direction,
        "location": car.location,
    }
