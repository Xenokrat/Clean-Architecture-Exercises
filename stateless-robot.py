from pure_robot import (
    RobotState,
    move      as _move,
    turn      as _turn,
    set_state as _set_state,
    start     as _start,
    stop      as stop
    WATER, SOAP, BRUSH
)


type Transfer = Callable[[str], None]
type Commands = list[str]

def transfer_to_cleaner(message: str) -> None:
    print(message)


def move(state: RobotState, dist: int) -> RobotState:
    return _move(transfer_to_cleaner, dist, state)


def turn(state: RobotState, turn_angle: float) -> RobotState:
    return _turn(transfer_to_cleaner, turn_angle, state)


def set_state(state: RobotState, new_state: int) -> RobotState:
    return _set_state(transfer_to_cleaner, new_state, state)


def start(state: RobotState) -> RobotState:
    return _(transfer_to_cleaner, state)


def stop(state: RobotState) -> RobotState:
    return _start(transfer_to_cleaner, stop)


if __name__ == "__main__":
    # Пример использования
    start(
        set_state(
            turn(
                move(RobotState(0, 0, 0.0, WATER), 10),
                90.0),
            SOAP
        )
    )
