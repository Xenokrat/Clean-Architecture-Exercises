import pure_robot


class RobotCommand:

    def __init__(self, input_state, command):
        self.state = input_state
        self.command = command


def transfer_to_cleaner(message):
    print(message)


##########

import queue as q
import threading

queue = q.Queue()
out_queue = q.Queue()


class ThreadRobo(threading.Thread):
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            command = self.queue.get()
            cleaner_state = command.state
            cmd = command.command.split(" ")
            if cmd[0] == "move":
                cleaner_state = pure_robot.move(
                    transfer_to_cleaner, int(cmd[1]), cleaner_state
                )
            elif cmd[0] == "turn":
                cleaner_state = pure_robot.turn(
                    transfer_to_cleaner, int(cmd[1]), cleaner_state
                )
            elif cmd[0] == "set":
                cleaner_state = pure_robot.set_state(
                    transfer_to_cleaner, cmd[1], cleaner_state
                )
            elif cmd[0] == "start":
                cleaner_state = pure_robot.start(transfer_to_cleaner, cleaner_state)
            elif cmd[0] == "stop":
                cleaner_state = pure_robot.stop(transfer_to_cleaner, cleaner_state)
            else:
                continue

            rez = RobotCommand(input_state=cleaner_state, command="RESULT")
            self.out_queue.put(rez)
            self.queue.task_done()


def command_to_queue(command):
    queue.put(command)
    chunk = out_queue.get()
    out_queue.task_done()
    return chunk


num_workers = 5

for i in range(num_workers):
    t = ThreadRobo(queue, out_queue)
    t.setDaemon(True)
    t.start()

if __name__ == "__main__":
    print("Robot server is running...")
    while True:
        pass  # Keep server alive
