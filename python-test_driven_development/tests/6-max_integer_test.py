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

    # Test for "max at the end" exists
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    # Test for "max at the beginning" exists
    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    # Test for "max in the middle" exists
    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 5, 4, 2]), 5)

    # Test for "one negative number in the list" exists
    def test_one_negative_number(self):
        self.assertEqual(max_integer([5, -3, 2]), 5)

    # Test for "only negative numbers in the list" exists
    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    # Test for "list of one element" exists
    def test_list_of_one_element(self):
        self.assertEqual(max_integer([10]), 10)

    # Test for "list is empty" exists
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()

