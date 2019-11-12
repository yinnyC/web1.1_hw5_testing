import unittest

from string_functions import *

class StringFunctionTests(unittest.TestCase):
    def test_default_greeting(self):
        """Tests for greet_by_name"""
        self.assertEqual(greet_by_name('Dani'), 'Hello, Meredith!')

# run the tests
if __name__ == '__main__':
    unittest.main()