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
    

if __name__ == "__main__":
    main()
