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

    # Test lorsque la liste est vide
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    # Test d'une liste avec des éléments positifs
    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    # Test d'une liste avec des éléments négatifs
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    # Test d'une liste avec un mélange de nombres positifs et négatifs
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    # Test d'une liste avec un seul élément
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    # Test d'une liste avec des éléments flottants
    def test_float_numbers(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 0.4]), 3.3)

    # Test d'une liste avec des éléments identiques
    def test_identical_numbers(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    # Test de types non valides dans la liste
    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a', 4])

# Exécution des tests
if __name__ == '__main__':
    unittest.main()
