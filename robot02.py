from dataclasses import dataclass
from enum import StrEnum
from typing import Any
import math

# Types
type Position = tuple[float, float]


class State(StrEnum):
    WATER = "WATER"
    SOAP = "SOAP"
    BRUSH = "BRUSH"


@dataclass
class Robot:
    position: Position
    angle: int
    state: State

    def __post_init__(self) -> None:
        self.angle = self.angle % 360


def main() -> None:
    commands = load_commands("./commands.txt")
    robot = init_robot()
    run_program(robot, commands)


def load_commands(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def init_robot() -> Robot:
    return Robot(position=(0.0, 0.0), state=State.WATER, angle=0)


def run_program(robot: Robot, commands: list[str]) -> None:
    for command in commands:
        parsed = parse_command(command)
        handle_command(robot, parsed)


def parse_command(command: str) -> tuple[str, Any]:
    parsed = command.split(" ")
    if len(parsed) > 2:
        raise ValueError(f"Invalid command number {parsed}")
    return tuple(map(lambda x: x.lower().strip(), parsed))


def handle_command(robot: Robot, parsed: str | tuple[str, Any]) -> None:
    match parsed:
        case "move", number:
            move(robot, float(number))
        case "turn", number:
            turn(robot, int(number))
        case "set", state:
            set(robot, state.upper())
        case ("start",):
            start(robot)
        case ("stop",):
            stop()
        case _:
            print(f"ERROR: robot has no command: {parsed}")


def set(robot: Robot, state: State) -> None:
    robot.state = state
    print(f"STATE {robot.state}")


def move(robot: Robot, distance: float) -> None:
    angle = robot.angle
    robot.position = (
        robot.position[0] + distance * math.cos(math.radians(angle)),
        robot.position[1] + distance * math.sin(math.radians(angle)),
    )
    print(f"POS {robot.position[0]:.2f} {robot.position[1]:.2f}")


def start(robot: Robot) -> None:
    print(f"START WITH {robot.state}")


def stop() -> None:
    print("STOP")


def turn(robot: Robot, angle: float) -> None:
    robot.angle += angle


if __name__ == "__main__":
    main()
