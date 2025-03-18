from typing import Callable
import pure_robot

type RobotFunc = tuple[str, Callable[[...], None]]

class RobotApi:
    impl_commands = set([
        "move",
        "turn",
        "set",
        "start",
        "stop",
    ])

    def __str__(self) -> str:
        if hasattr(self, "cleaner_start"):
            return str(self.cleaner_state)
        return "NOT SET"

    def setup(self, f_transfer):
        self.f_transfer = f_transfer

    def set_function(self, fn_name, fn):
        if fn_name not in self.impl_commands:
            return
        setattr(self, fn_name, fn)

    def make(self, command):
        if not hasattr(self, "cleaner_state"):
            self.cleaner_state = pure_robot.RobotState(0.0, 0.0, 0, pure_robot.WATER)

        cmd = command.split(" ")

        if not hasattr(self, cmd[0]):
            return self.cleaner_state

        if cmd[0] == "move":
            self.cleaner_state = self.move(
                self.f_transfer, int(cmd[1]), self.cleaner_state
            )
        elif cmd[0] == "turn":
            self.cleaner_state = self.turn(
                self.f_transfer, int(cmd[1]), self.cleaner_state
            )
        elif cmd[0] == "set":
            self.cleaner_state = self.set(
                self.f_transfer, cmd[1], self.cleaner_state
            )
        elif cmd[0] == "start":
            self.cleaner_state = self.start(self.f_transfer, self.cleaner_state)
        elif cmd[0] == "stop":
            self.cleaner_state = self.stop(self.f_transfer, self.cleaner_state)

        return self.cleaner_state

    def __call__(self, command):
        return self.make(command)


def transfer_to_cleaner(message):
    print(message)


def double_move(transfer, dist, state):
    return pure_robot.move(transfer, dist * 2, state)


api = RobotApi()
api.setup(transfer_to_cleaner)


if __name__ == "__main__":
    api = RobotApi()
    api.setup(transfer_to_cleaner)

    api.set_function("move",  double_move)
    api.set_function("turn",  pure_robot.turn)
    api.set_function("set",   pure_robot.set_state)
    api.set_function("stop",  pure_robot.stop)
    api.set_function("start", pure_robot.start)

    api("move 100")
    api("turn -90")
    api("set soap")
    api("start")

    api.set_function("move",  pure_robot.move)
    api("move 50")

    s = api("stop")
    print(s)
