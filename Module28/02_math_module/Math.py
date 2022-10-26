from math import pi


class MyMath:
    @classmethod
    def circle_len(cls, radius):
        result = 2 * pi * radius
        return round(result, 3)

    @classmethod
    def circle_sq(cls, radius):
        result = pi * radius**2
        return round(result, 3)

    @classmethod
    def sphere_sq(cls, radius):
        result = 4 * pi * radius**2
        return round(result, 3)

    @classmethod
    def cube_vol(cls, value):
        result = value**3
        return round(result, 3)
