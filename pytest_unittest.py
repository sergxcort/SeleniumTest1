__author__ = 'Sergey'
import pytest
from pytest_program import parse_input, output


def test_currency_is_EUR_or_USD__only():
    assert parse_input("100 eur") == (81, 0, 'USD')