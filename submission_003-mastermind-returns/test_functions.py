import unittest
from unittest.mock import patch
import sys
import io
from io import StringIO
import mastermind
#from mastermind import * (imports everything(all))



class TestFunctions(unittest.TestCase):
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    def test_create_code(self):
        for i in range(100):
            code = mastermind.create_code()
            self.assertEqual(len(code), 4)
            if 0 or 9 in code:
                self.assertEqual(1,0)

    def test_check_correctness(self):
        self.assertEqual(mastermind.check_correctness(6,4),True)
        self.assertEqual(mastermind.check_correctness(6,2),False)

    @patch('sys.stdin',StringIO('123\n12345\n1234'))
    def test_get_input(self):
        self.assertEqual(mastermind.get_input(),'1234')

    def test_take_turn(self):
        self.assertEqual(mastermind.take_turn([1,2,3,4],'1234'),(4,0))
        self.assertEqual(mastermind.take_turn([1,2,3,4],'1254'),(3,0))
        self.assertEqual(mastermind.take_turn([1,2,3,4],'5678'),(0,0))


if __name__ == '__main__':
    unittest.main()