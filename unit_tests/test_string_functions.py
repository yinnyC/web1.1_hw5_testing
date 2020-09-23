import pytest

from string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremya!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert expected == actual

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert expected == actual

def test_reverse_1():
    """Test reversing a string."""
    expected = ''
    actual = ''
    assert expected == actual

def test_reverse_2():
    """Test reversing a string."""
    expected = ''
    actual = ''
    assert expected == actual

def test_reverse_words_1():
    """Test reversing words in a string."""
    expected = ''
    actual = ''
    assert expected == actual

def test_reverse_words_2():
    """Test reversing words in a string."""
    expected = ''
    actual = ''
    assert expected == actual

def test_sarcastic_1():
    """Test sarcastic-ifying a string."""
    expected = ''
    actual = ''
    assert expected == actual

def test_sarcastic_2():
    """Test sarcastic-ifying a string."""
    expected = ''
    actual = ''
    assert expected == actual

# run the tests
if __name__ == '__main__':
    unittest.main()