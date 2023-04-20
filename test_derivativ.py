from Quadratic import Quadratic
from Derivativ import Derivativ

def test_create_derivativ():
    f = Quadratic(1, 2, 3)
    df = Derivativ(f)

def test_evaluate_derivativ():
    f = Quadratic(1, 0, 0)
    # f = x**2 ; dfdx = 2x
    # f(2) = 4
    df = Derivativ(f)
    assert abs(df(2) - 4) < 1e-6

# hvis du vil bare teste denne fil
# python -m pytest -v test_derivativ.py