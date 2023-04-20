from math import pi, sqrt
import pytest
    
class Sphere:
    def __init__(self, radius):
        print("Start __init__")

        #assert radius >= 0, "Radius cann't be negativt!"
        if radius < 0:
            raise ValueError("Radius cann't be negativt!")
        print("Before setting")
        self._radius = radius
        print("After setting")

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, radius):
        print("Inside setting")
        self._radius = radius
    
    @property # den hjelper ved å ta bort ()
    def areal(self):
        return 4*pi*self._radius**2
    @areal.setter # den hjelper ved å endre radius
    def areal(self, areal):
        if areal < 0:
            raise ValueError("Area cann't be negativt!")
        self._radius = sqrt(areal/(4*pi))
    
    @property # den hjelper ved å ta bort () 
    def volum(self):
        return self.areal()*self._radius/3

    @property
    def radius(self):
        return self._radius

    def __str__(self):
        return f"{self.__class__.__name__} with radius {self._radius}"

def test_radius():
    fotball = Sphere(2)
    areal = fotball.areal
    fotball.areal = areal
    assert abs(fotball.radius - 2) < 1e-12

def test_areal_negativt():
    s = Sphere(2)
    with pytest.raises(ValueError):
        s.areal = -1
    
if __name__ == "__main__":
    #fotball = Sphere(2)
    #print(f"The sphere volume is : {fotball.volum}")
    #print(fotball)

    #test_radius()

    #test_areal_negativt()

    s = Sphere(3)