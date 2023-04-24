import pytest
from palindrom import is_palindrom

def test_palindrom():
    assert is_palindrom("bob")

def test_not_palindrom():
    assert not is_palindrom("mung")

def test_palindrom_upper_lower_case():
    assert is_palindrom("Bob")

def test_is_palindrom_with_spaces():
    assert is_palindrom("Do geese see God")

def test_is_palindrom_raises_ValueError_for_numbers():
    with pytest.raises(ValueError):
        assert is_palindrom(110011)

@pytest.mark.parametrize("x", ["bob", "Bob", "Madam", "Do geese see God"])
def test_is_palindrom(x):
    assert is_palindrom(x)

@pytest.mark.parametrize("x, value", [("bob", True), ("mung", False)])
def test_is_palindrom2(x, value):
    assert is_palindrom(x) == value 

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

if __name__ == "__main__":
    test_is_palindrom2("bob", True)
    test_is_palindrom2("mung", False)