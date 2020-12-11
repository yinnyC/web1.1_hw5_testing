import pytest

from .string_functions import *


def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'
    name = "Jeremy"
    # Step 2: Decide what the expected outcome is for the scenario
    expected = "Hello, Jeremy!"

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name("Jeremy")

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected


def test_greeting_dani():
    """Test for greet_by_name"""
    expected = "Hello, Dani!"
    actual = greet_by_name("Dani")
    assert actual == expected


def test_reverse_long():
    """Test reversing a long string."""
    expected = "!niY olleH"
    actual = reverse("Hello Yin!")
    assert actual == expected


def test_reverse_short():
    """Test reversing a short string."""
    expected = "iH"
    actual = reverse("Hi")
    assert actual == expected


def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = "niYniYniY"
    actual = reverse_words("YinYinYin")
    assert actual == expected


def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = "niY"
    actual = reverse_words("Yin")
    assert actual == expected


def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = "ReTuRnS tHe SaRcAsTiC vErSiOn Of A sTrInG"
    actual = sarcastic("rEtUrNs ThE sArCaStIc VeRsIoN oF a StRiNg")
    assert actual == expected


def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = "ReTuRnS"
    actual = sarcastic("rEtUrNs")
    assert actual == expected


def test_find_longest_word():
    """Test find_longest_word in a string"""
    expected = ""
    actual = find_longest_word("")
    assert actual == expected


# run the tests
if __name__ == "__main__":
    unittest.main()