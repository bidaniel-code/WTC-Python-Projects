from tests.test_main import MyTestCase
import unittest
import robot
from world.text.world import *
from world.turtle.world import *
import world.obstacles 
from io import StringIO
from test_base import captured_io

class MyTestCase(unittest.TestCase):
    def test_get_obstacles(self):
        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            world.obstacles.random.randint = lambda a, b: 1
            obs_list = world.obstacles.get_obstacles()

        answer = [(1, 1)]
        self.assertEqual(obs_list,answer)