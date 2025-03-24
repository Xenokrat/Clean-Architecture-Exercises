"""
Класс Robot, его описание и управление
"""

from enum import StrEnum
from typing import Callable
import math

from .robot_utils import Angle, Position
from .robot_commands import Command


class RobotState(StrEnum):
    WATER = "WATER"
    SOAP = "SOAP"
    BRUSH = "BRUSH"


class Robot:
    def __init__(self, position: Position, state: RobotState, angle: Angle) -> None:
        self._position = position
        self._state = state
        self._angle = angle

    def move(self, distance: float) -> str:
        self._position = (
            self._position[0] + distance * math.cos(math.radians(self._angle.value())),
            self._position[1] + distance * math.sin(math.radians(self._angle.value())),
        )
        return f"POS {self._position[0]:.2f} {self._position[1]:.2f}"

    def set(self, new_state: RobotState) -> str:
        self._state = new_state
        return f"STATE {self._state}"

    def start(self) -> str:
        return f"START WITH {self._state}"

    def stop(self) -> str:
        return "STOP"

    def turn(self, angle: Angle) -> str:
        self._angle += angle
        return f"ANGLE {self._angle}"

    def handle_command(self, parsed: Command, action: Callable[[str], None]) -> str:
        match parsed:
            case ["move", number]:
                action(self.move(float(number)))
            case ["turn", number]:
                action(self.turn(Angle(float(number))))
            case ["set", state]:
                action(self.set(state.upper()))
            case ["start"]:
                action(self.start())
            case ["stop"]:
                action(self.stop())
            case _:
                print(f"ERROR: robot has no command: {parsed}")

    def handle_commands(
        self, list_parsed: list[Command], action: Callable[[str], None]
    ) -> str:
        for p in list_parsed:
            self.handle_command(p, action)
