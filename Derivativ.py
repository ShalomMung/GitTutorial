
class Derivativ:
    def __init__(self, f):
        self._f = f
    
    def __call__(self, x, h=1e-6):
        return (self._f(x + h) - self._f(x - h))/(2*h)