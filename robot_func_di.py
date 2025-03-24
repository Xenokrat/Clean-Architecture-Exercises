from typing import Callable

import pure_robot as pr


type Transfer = Callable[[str], None]

type Arg = int | float | None

type RobotFunction = Callable[[Transfer, Arg, pr.RobotState], pr.RobotState]


def call_robot_function(
    robot_fn: RobotFunction,
    transfer: Transfer,
    arg: Arg,
    state: pr.RobotState,
) -> pr.RobotState:
    if arg is None:
        return robot_fn(transfer, state)
    return robot_fn(transfer, arg, state)


# Выполнить серию текстовых команд
type RobotMake = Callable[[Transfer, list[str], pr.RobotState], pr.RobotState]


def call_robot_make(
    make_fn: RobotMake,
    transfer: Transfer,
    code: list[str],
    state: pr.RobotState,
) -> pr.RobotState:
    return make_fn(transfer, code, state)


# Пример
if __name__ == "__main__":
    state = pr.RobotState(0, 0, 0.0, pr.WATER)
    state = call_robot_function(pr.move, pr.transfer_to_cleaner, 10, state)
    state = call_robot_function(pr.turn, pr.transfer_to_cleaner, 60.0, state)
    state = call_robot_function(pr.set_state, pr.transfer_to_cleaner, pr.BRUSH, state)
    state = call_robot_function(pr.move, pr.transfer_to_cleaner, 10, state)
    print(state)
