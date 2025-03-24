"""
Получить коммады для класса Robot из источника данных
"""

from typing import Protocol

type Command = tuple[str, float | int] | tuple[str]


class PCommandReader(Protocol):
    def run(self) -> list[Command]: ...


class CommandReader:
    def __init__(self, path: str) -> None:
        self.path = path

    def run(self) -> list[Command]:
        self._read()
        for command in self._get_commands():
            parsed = command.split(" ")
            parsed = list(map(lambda x: x.lower().strip(), parsed))
            if len(parsed) > 2:
                raise ValueError(f"Invalid command number {parsed}")
            return parsed

    def _read(self) -> None:
        with open(self.path, "r") as f:
            self._str_commands = f.readlines()

    def _get_commands(self) -> list[str]:
        return self._str_commands
