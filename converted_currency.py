from pytest_program import parse_input, output
import pytest
parse = pytest.mark.parse
output_marker = pytest.mark.output
 
 
@pytest.mark.parametrize(("string", "data"), [
    ("100 EUR", (122, 0, "USD")), 
    ("100 USD", (81, 0, "EUR")), 
    ("99 USD", (80, 19, "EUR")), 
    ("99 eur", (120, 78, "USD"))])
def test_currency_exchange(string, data):
    assert parse_input(string) == data
 
@parse
class TestCovertorParse:    
    def test_no_arguments_passed(self):
        assert parse_input("") == (None,None,None)
 
    def test_more_than_100_cents(self):
        pytest.skip("skip this test")
 
@output_marker
class TestCovertorOutput:
    def test_passed_argumnets_have_cents(self):
        assert output(None, None, None) == "You did mistake during input"
 
    def test_passed_argumnets_have_cents1(self):
        assert output(100, 0, "USD") == "100 USD"
 
    def test_passed_argumnets_have_no_cents(self):
        assert output(89, 50, "EUR") == "89 EUR and 50 cents"