from typing import Callable, TypeVar

import pure_robot as pr

S = TypeVar("S")
A = TypeVar("A")

type Processor[A, S] = Callable[[S], tuple[A, S]]
type Func[A, S] = Callable[[A], "StateMonad[A, S]"]


class StateMonad[A, S]:

    def __init__(self, processor: Processor[A, S]):
        self.processor = processor

    def run(self, state: S) -> tuple[A, S]:
        return self.processor(state)

    def bind(self, f: Func[A, S]) -> "StateMonad[A, S]":
        def new_func(state):
            result, new_state = self.processor(state)
            return f(result).run(new_state)

        return StateMonad(new_func)

    @staticmethod
    def unit(value) -> "StateMonad[A, S]":
        return StateMonad(lambda s: (value, s))


def move(transfer_func, distance: int) -> StateMonad[None, pr.RobotState]:
    return StateMonad(lambda s: (None, pr.move(transfer_func, distance, s)))


def turn(transfer_func, angle: float) -> StateMonad[None, pr.RobotState]:
    return StateMonad(lambda s: (None, pr.turn(transfer_func, angle, s)))


def set_state(transfer_func, state: int) -> StateMonad[None, pr.RobotState]:
    return StateMonad(lambda s: (None, pr.set_state(transfer_func, state, s)))


def start(transfer_func) -> StateMonad[None, pr.RobotState]:
    return StateMonad(lambda s: (None, pr.start(transfer_func, s)))


def stop(transfer_func) -> StateMonad[None, pr.RobotState]:
    return StateMonad(lambda s: (None, pr.stop(transfer_func, s)))


if __name__ == "__main__":

    def transfer_to_cleaner(message: str):
        print(message)

    initial_state = pr.RobotState(0, 0, 0.0, pr.WATER)

    program = (
        move(transfer_to_cleaner, 10)
        .bind(lambda _: turn(transfer_to_cleaner, -90))
        .bind(lambda _: set_state(transfer_to_cleaner, pr.SOAP))
        .bind(lambda _: move(transfer_to_cleaner, 50))
        .bind(lambda _: stop(transfer_to_cleaner))
    )

    result, final_state = program.run(initial_state)
    print(final_state)
