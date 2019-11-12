import unittest

from string_functions import *

class StringFunctionTests(unittest.TestCase):
    def test_greeting(self):
        """Tests for greet_by_name"""
        self.assertEqual(greet_by_name('Jeremy'), 'Hello, Jeremy!')
        self.assertEqual(greet_by_name('Dani'), 'Hello, Dani!')

    def test_reverse(self):
        """Test reversing a string."""
        pass

    def test_reverse_words(self):
        """Test reversing words in a string."""
        pass

    def test_sarcastic(self):
        """Test sarcastic-ifying a string."""
        pass

# run the tests
if __name__ == '__main__':
    unittest.main()