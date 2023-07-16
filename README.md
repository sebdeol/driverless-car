# README

## Driverless Car Application

## Introduction

This is the GitHub repository hosting the code for the Driverless Car application.

This application replicates and simulates a driverless car alongside its various systems and functionalities.

Follow the steps below to set up and run the python application on your local machine.

## Installation

The application has been developed and tested with Python 3.11.
Ensure that both [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) are installed on your computer before con.

### Instructions to execute the Driverless Car Application

1) Open your preferred terminal application and clone the repository:

```bash
git clone git@github.com:sebdeol/driverless-car.git
```

2) Navigate to the driverless-car folder:

```bash
cd driverless-car
```

3) Install the project dependencies:
```bash
python3 -m pip install -r requirements.txt
```

4) Run the application:
```bash
python3 app/car.py
```

5) If you successfully followed the instructions, the application will start displaying the logs of the various systems like below:

```bash
❯❯❯ python3 app/car.py
Calculating new route...
Routing to [100, 72]
Engine controlled to set speed to 60
Car speed set to 60
Steering adjusted to direction 37.05652818940959
Car direction set to 37.05652818940959
Object detected: {'type': 'Obstacle', 'location': [69, -31]}
Avoiding obstacle at [69, -31]
```


If you want to test the application, you can run the tests with the command below:

```bash
python3 -m pytest -v
```

## Project Design and Rationale

This project was designed to replicate the systems found in a real-world autonomous car.

The main `Car` class integrates all the subsystems: `AutonomousNavigation`, `EnvironmentalPerception`, and `UserInteraction`.

- The `AutonomousNavigation` class handles the key functionality of path planning and navigation. In a real-world scenario, an autonomous vehicle needs to calculate and follow a safe route to reach its destination. The car must continuously evaluate its route in response to changing conditions, such as traffic or roadwork.

- The `EnvironmentalPerception` class represents the various sensors and perception systems found in autonomous vehicles. These systems are critical to identify and react to environmental factors such as obstacles. In this design, `EnvironmentalPerception` processes sensors data and handles object detection. Although simplified and randomised for this assignment, the class represents the crucial role perception systems play in avoiding collisions thus ensuring safe navigation.

- The `UserInteraction` class represent the interface between the autonomous car and the user. Although autonomous cars are self-driving, there is still a need for various user interactions. This interaction can range from setting preferences like temperature or seat heating.

This classes have been developed with encapsulation and separation of concerns in mind. This allows for better maintainability and extensibility down the line.

Automated tests have been written with `pytest` for each class to ensure their functionality works as expected.

## Future Improvements
With more time, here are a few things that could be improved:

Navigation Algorithms: The navigation algorithm could be improved by implementing a more advanced path-finding algorithm like Dijkstra's or A*.

Detailed Environment and Sensor Simulation: Currently, object detection is randomised for simplicity.
In a real-world scenario, a detailed environment with real obstacles would make the simulation more engaging.

Support more User Interactions: The UserInteraction class could be extended to support more commands and provide a richer interaction for the user such as phone interaction, radio support and why not video games like in a Tesla car.

Machine Learning Integration: The use of machine learning could improve decision-making, object detection, and user preferences adaptation, leading to a more intelligent car.

These improvements could bring the simulation closer to the complexity of a real driverless car system while maintaining the code's modularity and extensibility.