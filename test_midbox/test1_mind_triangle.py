import pytest
import math
from shapes import Circle, Triangle

@pytest.mark.parametrize("radius, expected", [(0, 0), (1, math.pi), (5, 78.53981633974483)])
def test_circle_area(radius, expected):
    assert circle_area(radius) == expected

@pytest.mark.parametrize("a, b, c, expected", [(3, 4, 5, 6.0), (5, 5, 5, 10.825317547305483)])
def test_triangle_area(a, b, c, expected):
    assert triangle_area(a, b, c) == expected

@pytest.mark.parametrize("a, b, c, expected", [(3, 4, 5, True), (3, 4, 6, False)])
def test_is_right_triangle(a, b, c, expected):
    assert is_right_triangle(a, b, c) == expected

def test_circle_class():
    circle = Circle(5)
    assert circle.radius == 5
    assert circle.area() == 78.53981633974483

def test_triangle_class():
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5
    assert triangle.area() == 6.0
    assert triangle.is_right() == True