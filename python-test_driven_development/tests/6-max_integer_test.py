#!/usr/bin/python3
"""
la fonction qui fait les trucs
"""


import unittest
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class Test_max_integer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_ineger([1,2], 2)
    def test_2(self):
        self.assertEqual(max_ineger([1,2,3,-5], 3)
    def test_3(self):
        self.assertIsNone(max_integer([])
    def test_4(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    def test_5(self):
        self.asserEqual(max_integer([-1, -3, -4, -2]), -1) 
if __name__ == '__main__':
    unittest.main()
