from Quadratic import Quadratic

def test_str():
    a = 2
    b = 1
    c = 4
    f = Quadratic(a, b, c)
    assert str(f) == f"{a}x**2 + {b}x + {c}"

def test_is_callable():
    f = Quadratic(1, 2, 3)
    assert callable(f)

# kjør dette i terminal
# python -m pytest -v