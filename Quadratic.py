
class Quadratic:
    degree = 2

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f"{self._a}x**2 + {self._b}x + {self._c}"
    
    def evaluate(self, x):
        return self._a*x**2 + self._b*x + self._c
    
    def __call__(self, x):
        return self.evaluate(x)

if __name__ == "__main__":
    f = Quadratic(2, 1, 4)
    print(f)
    #print(f"f(1) = {f.evaluate(1)}")

    # f.evaluate(1) --> f(1)?
    # y = f(1) --> def __call__(self)
    # after __call__
    y = f(1)
    print(f"f(1) = {f(1)}")
    

