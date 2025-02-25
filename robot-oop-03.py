from typing import Self 
from enum import StrEnum
import math

type Position = tuple[float, float]


class CommandReader:
    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> None:
        with open(self.path, 'r') as f:
            self._str_commands = f.readlines()

    def get_commands(self) -> list[str]:
        return self._str_commands


class Angle:
    def __init__(self, value: int) -> None:
        self._angle = value % 360

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Angle):
            raise ValueError(f"{other} should be instance of Angle!")
        return Angle(self._angle + other._angle)

    def __iadd__(self, other: Self) -> Self:
        if not isinstance(other, Angle):
            raise ValueError(f"{other} should be instance of Angle!")
        self._angle = (self._angle + other._angle) % 360
        return self

    def __str__(self) -> str:
        return str(self._angle)

    def value(self) -> int:
        return self._angle


class RobotState(StrEnum):
    WATER = "WATER"
    SOAP = "SOAP"
    BRUSH = "BRUSH"


class Robot:
    def __init__(
        self, 
        position: Position, 
        state: RobotState,
        angle: Angle
    ) -> None:
        self._position = position
        self._state = state
        self._angle = angle

    def move(self, distance: float) -> None:
        # NOTE: This is ugly af
        self._position = (
            self._position[0] + distance * math.cos(math.radians(self._angle.value())),
            self._position[1] + distance * math.sin(math.radians(self._angle.value()))
        )
        print(f"POS {self._position[0]:.2f} {self._position[1]:.2f}")

    def set(self, new_state: RobotState) -> None:
        self._state = new_state
        print(f"STATE {self._state}")

    def start(self) -> None:
        print(f"START WITH {self._state}")
    
    def stop(self) -> None:
        print("STOP")
    
    def turn(self, angle: Angle) -> None:
        self._angle += angle
        print(f"ANGLE {self._angle}")


class Handler:
    def __init__(self, commands: CommandReader, robot: Robot) -> None:
        self._commands = commands
        self._robot = robot

    def run(self) -> None:
        self._commands.read()
        for command in self._commands.get_commands():
            parsed = command.split(' ')
            parsed = list(map(lambda x: x.lower().strip(), parsed))
            if len(parsed) > 2:
                raise ValueError(f"Invalid command number {parsed}")
            self._handle_command(parsed)

    def _handle_command(self, parsed: list[str]) -> None:
        match parsed:
            case ["move", number]:
                self._robot.move(float(number))
            case ["turn", number]:
                self._robot.turn(
                    Angle(float(number))
                )
            case ["set", state]:
                self._robot.set(state.upper())
            case ["start"]:
                self._robot.start()
            case ["stop"]:
                self._robot.stop()
            case _:
                print(f"ERROR: robot has no command: {parsed}")


def main() -> None:
    commands = CommandReader("./commands.txt")
    robot = Robot(position=(0.0, 0.0),
                  state=RobotState.WATER,
                  angle=Angle(0))
    handler = Handler(commands, robot)
    handler.run()


if __name__ == "__main__":
    main()
