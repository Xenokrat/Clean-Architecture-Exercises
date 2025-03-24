import io
import sys
import unittest
import unittest.mock

from robot import *


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot((0.0, 0.0), RobotState.WATER, Angle(0))

    def test_test(self):
        self.assertEqual(1, 1)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_prints_move(self, mock_stdout):
        self.robot.move(100)
        self.assertEqual(self.robot._position[0], 100)
        self.assertEqual(self.robot._position[1], 0)
        self.robot.turn(Angle(-90))
        self.robot.move(50)
        self.assertEqual(self.robot._position[0], 100)
        self.assertEqual(self.robot._position[1], 50)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_prints_new_state(self, mock_stdout):
        new_state = RobotState.WATER
        self.robot.set(new_state)
        self.assertEqual(mock_stdout.getvalue(), "STATE WATER\n")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_prints_start(self, mock_stdout):
        self.robot._state = RobotState.SOAP
        self.robot.start()
        self.assertEqual(mock_stdout.getvalue(), "START WITH SOAP\n")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_prints_stop(self, mock_stdout):
        self.robot.stop()
        self.assertEqual(mock_stdout.getvalue(), "STOP\n")

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_prints_turn(self, mock_stdout):
        self.robot.turn(Angle(-90))
        self.assertEqual(self.robot._angle.value(), 270)
        self.robot.turn(Angle(500))
        self.assertEqual(self.robot._angle.value(), 50)


if __name__ == "__main__":
    unittest.main()
