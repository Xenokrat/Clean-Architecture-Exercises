from typing import Callable
import pure_robot as pr

type Program = list[str]
type Transfer = Callable[[str], None]

commands_dict = {
    "move" : pr.move,
    "turn" : pr.turn,
    "set"  : pr.set_state,
    "start": pr.start,
    "stop" : pr.stop,
}


def transfer_to_cleaner(message):
    print(message)
        

def push_command(
    program: Program,
    state: pr.RobotState,
    transfer: Transfer,
    arg: str
) -> pr.RobotState:
    try:
        match arg:

            case "move" | "turn":
                value = float(program.pop())
                func = commands_dict[arg]
                return func(transfer, value, state)

            case "set":
                value = str(program.pop())
                func = commands_dict[arg]
                return func(transfer, value, state)

            case "start" | "stop":
                func = commands_dict[arg]
                return func(transfer, state)

            case _:
                program.append(arg)
                return state

    except (ValueError, KeyError):
        return state
        

def execute_program(
    program_txt: str,
    state      : pr.RobotState,
    transfer   : Transfer,
) -> None:
    for command in program_txt.split(" "):
        command = command.strip()
        state = push_command(program, state, transfer, command)
        print(state)
    

################# Client's Side ###################
program: Program = []
transfer = transfer_to_cleaner
state = pr.RobotState(0, 0, 0.0, pr.WATER)

program_txt = "100 move -90 turn soap set start 50 move stop"
execute_program(program_txt, state, transfer)
