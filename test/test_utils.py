from fizzbot.resources.utils import validate_data, fizz_buzz
import pytest


def test_if_is_fizzbuzz():
    result = fizz_buzz("15")
    assert result == "15 is fizzbuzz"


def test_if_is_fizz():
    result = fizz_buzz("3")
    assert result == "3 is fizz"


def test_if_is_buzz():
    result = fizz_buzz("5")
    assert result == "5 is buzz"


def test_if_is_not_a_fizzbuzz():
    result = fizz_buzz("4")
    assert result == 4


def test_if_is_a_valid_number():
    result = validate_data("11")
    assert result == 11


def test_if_is_a_invalid_number():
    result = validate_data("abc")
    assert result == "Your entry must be an integer number and not more than 280 characters"