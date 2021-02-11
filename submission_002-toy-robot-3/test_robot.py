import unittest
import robot
from io import StringIO
from test_base import captured_io


class MyTestCase(unittest.TestCase):
    def test_do_forward(self):
        with captured_io(StringIO("HAL\nforward 10\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down..""", output) 

    def test_do_back(self):
        with captured_io(StringIO("HAL\nback 10\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_do_right_turn(self):
        with captured_io(StringIO("HAL\nright\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_do_left_turn(self):
        with captured_io(StringIO("HAL\nleft\noff\n")) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_do_sprint(self):
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

    def test_do_replay(self):
        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,25).
 > HAL moved forward by 5 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_do_replay_silent(self):
        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay silent\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_do_replay_reversed(self):
        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay reversed\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)

    def test_do_replay_reversed_silent(self):
        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay reversed silent\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""", output)



if __name__ == '__main__':
    unittest.main()    