# Модуль Robot


## Robot

Основной модуль, содержащий класс робота, и описание его состояний

## Robot_Commands

Предоставляет интерфейс для загрузки комманд для выполнения роботом

## Robot_Utils

Предоставляет дополнительные классы-помошники, для управления поведением робота:

- `class Angle` - класс управляющий углом поворота
- `type Position` - положение робота в пространстве

## Usage

```python
from robot import Robot, RobotState, Angle, CommandReader


def main() -> None:
    commands = CommandReader("./commands.txt")
    robot = Robot(
        position=(0.0, 0.0),
        state=RobotState.WATER,
        angle=Angle(0)
    )

    cmd = commands.run()
    robot.handle_commands(cmd, print)
```
