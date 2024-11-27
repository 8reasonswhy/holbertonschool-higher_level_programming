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

class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        self.assertTrue(max_integer([1, 2, 3, 4, 5]) == 5)

    def test_max_at_beginning(self):
        self.assertTrue(max_integer([5, 4, 3, 2, 1]) == 5)

    def test_max_in_middle(self):
        self.assertTrue(max_integer([1, 3, 5, 4, 2]) == 5)

    def test_one_negative_number(self):
        self.assertTrue(max_integer([5, -3, 2]) == 5)

    def test_only_negative_numbers(self):
        self.assertTrue(max_integer([-5, -4, -3, -2, -1]) == -1)

    def test_list_of_one_element(self):
        self.assertTrue(max_integer([10]) == 10)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()

