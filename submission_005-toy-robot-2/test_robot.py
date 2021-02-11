import unittest
import robot
from io import StringIO
from robot import name_robot
from test_base import captured_io
from unittest.mock import patch
import sys

class MyTestCase(unittest.TestCase):
    @patch("sys.stdin", StringIO("hal\njay\n"))
    def test_name_robot(self):
        self.assertEqual(robot.name_robot(), "hal".upper())
        self.assertEqual(robot.name_robot(), "jay".upper()) 
    
    def test_off_command(self):
        with captured_io(StringIO("HAL\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_help_command(self):
        with captured_io(StringIO("HAL\nhelp\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - Moves the robot forward the number of steps you give it
BACK - Moves the robot backwards the number of steps you give it
RIGHT - turns the robot 90% to the right
LEFT - turns the robot 90% to the left
SPRINT - Move the robot forward x amount of times
HAL: What must I do next? HAL: Shutting down..""", output)
 
    def test_forward_command(self):
        with captured_io(StringIO("HAL\nforward 10\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_back_command(self):
        with captured_io(StringIO("HAL\nback 10\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_right_command(self):
        with captured_io(StringIO("HAL\nright\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_left_command(self):
        with captured_io(StringIO("HAL\nleft\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_sprint_command(self):
        with captured_io(StringIO("HAL\nsprint 5\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,15).
HAL: What must I do next? HAL: Shutting down..""", output)


if __name__ == '__main__':
    unittest.main()