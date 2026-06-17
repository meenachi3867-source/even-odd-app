from app import check_even_odd

def test_even():
    assert check_even_odd(10) == "Even"

def test_odd():
    assert check_even_odd(7) == "Odd"
