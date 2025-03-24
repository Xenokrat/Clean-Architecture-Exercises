"""
API управления роботом

Начальное состояние робота
`RobotState`:
    x: int       - позиция по оси x
    y: int       - позиция по оси y
    angle: float - текущий угол поворота
    state:       - текущее состояние робота:
        WATER - вода
        SOAP  - мыло
        BRUSH - щётка

Доступные команды:
move [dist: int] - двигает робота на dist вперёд
turn [angle: float] - поворачивает робота на угол angle
set  [state: WATER | SOAP | BRUSH] - устанавливает робота в состояние state
start - начало работы
stop - конец работы

`make`:
    Функця для запуска выполнения команд роботом
    Принимает:
        - Transfer - функцию
        - Набор `команд` в виде строк `команда [значение агрумента]`
        - Начальное состояние `RobotState`
"""

from pure_robot import RobotState, make as _make, WATER, SOAP, BRUSH


# Как клиент использует информацию о работе робота
type Transfer = Callable[[str], None]
type Commands = list[str]

def transfer_to_cleaner(message: str) -> None:



# API Команд
def make(
    transfer: Transfer,
    code: Commands,
    state: RobotState
) -> RobotState:
    return _make(transfer, code, state)


"""
Пример использования
"""
def main() -> None:
    commands = [
        "move 10",
        "turn 90",
        "set soap",
        "start",
        "move 5",
        "stop"
    ]
    robot = RobotState(0, 0, 0.0, WATER)
    robot = make(
        transfer_to_cleaner,
        commands,
        robot
    )
    print(robot)


if __name__ == "__main__":
    main()
