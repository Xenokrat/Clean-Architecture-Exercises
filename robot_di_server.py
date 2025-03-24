from typing import Callable
import pure_robot

type Transfer = Callable[[str], None]


# класс Чистильщик API
class CleanerApi:

    # конструктор
    # расширим его параметрами
    def __init__(
        self,
        robot_cls: pure_robot.RobotState,
        position_x: int,
        position_y: int,
        angle: float,
        initial_state: int,
        transfer: Transfer,
    ):
        self.cleaner_state = robot_cls(
            position_x,
            position_y,
            angle,
            initial_state,
        )
        self.transfer = transfer

    def get_x(self):
        return self.cleaner_state.x

    def get_y(self):
        return self.cleaner_state.y

    def get_angle(self):
        return self.cleaner_state.angle

    def get_state(self):
        return self.cleaner_state.state

    def activate_cleaner(self, code):
        for command in code:
            cmd = command.split(" ")
            if cmd[0] == "move":
                self.cleaner_state = pure_robot.move(
                    self.transfer, int(cmd[1]), self.cleaner_state
                )
            elif cmd[0] == "turn":
                self.cleaner_state = pure_robot.turn(
                    self.transfer, int(cmd[1]), self.cleaner_state
                )
            elif cmd[0] == "set":
                self.cleaner_state = pure_robot.set_state(
                    self.transfer, cmd[1], self.cleaner_state
                )
            elif cmd[0] == "start":
                self.cleaner_state = pure_robot.start(self.transfer, self.cleaner_state)
            elif cmd[0] == "stop":
                self.cleaner_state = pure_robot.stop(self.transfer, self.cleaner_state)
