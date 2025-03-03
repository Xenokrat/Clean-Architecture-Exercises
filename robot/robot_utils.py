"""
Дополнительные фичи для управления роботом:
    - Angle: класс для управления углом поворота
"""
from typing import Self


type Position = tuple[float, float]


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


