from robot_di_server import CleanerApi
import pure_robot


def transfer_to_cleaner(message):
    print(message)


# Вставка завпсимостей
cleaner_api = CleanerApi(
    robot_cls=pure_robot.RobotState,
    position_x=0,
    position_y=0,
    angle=0.0,
    initial_state=pure_robot.WATER,
    transfer=transfer_to_cleaner,
)

cleaner_api.activate_cleaner(
    ("move 100", "turn -90", "set soap", "start", "move 50", "stop")
)

print(
    cleaner_api.get_x(),
    cleaner_api.get_y(),
    cleaner_api.get_angle(),
    cleaner_api.get_state(),
)
