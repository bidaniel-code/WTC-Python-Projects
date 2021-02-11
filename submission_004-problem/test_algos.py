import unittest
import super_algos


class MyTestCase(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(-1, super_algos.find_min([]))
        self.assertEqual(1, super_algos.find_min([3,5,6,1,10]))
        self.assertEqual(3, super_algos.find_min([3]))
        self.assertEqual(22, super_algos.find_min([22]))
        self.assertEqual(789, super_algos.find_min([789]))
        self.assertEqual(-5, super_algos.find_min([77,12,-5,0,3]))


    def test_sum_all(self):
        self.assertEqual(15, super_algos.sum_all([1,2,3,4,5]))
        self.assertEqual(3, super_algos.sum_all([3]))
        self.assertEqual(22, super_algos.sum_all([22]))
        self.assertEqual(789, super_algos.sum_all([789]))
        self.assertEqual(-17, super_algos.sum_all([-5,-3,-9]))
        self.assertEqual(-1, super_algos.sum_all([-1]))


    def test_ind_possible_strings(self):
        self.assertEqual(['a', 'b'], super_algos.find_possible_strings(['a','b'], 1))
        self.assertEqual(['aa','ab','ba','bb'], super_algos.find_possible_strings(['a','b'], 2))
        self.assertEqual(['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'], super_algos.find_possible_strings(['a','b'], 3))
        self.assertEqual(['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb'], super_algos.find_possible_strings(['a','b'], 4))


if __name__ == '__main__':
    unittest.main()    