import math

def circle_area(radius):
    """
    Вычисляет площадь круга по его радиусу.
    """
    return math.pi * radius**2

def triangle_area(a, b, c):
    """
    Вычисляет площадь треугольника по трем его сторонам, используя формулу Герона.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def is_right_triangle(a, b, c):
    """
    Проверяет, является ли треугольник с заданными сторонами прямоугольным.
    """
    sides = [a, b, c]
    sides.sort()
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

class Shape:
    """
    Базовый класс для геометрических фигур.
    """
    def area(self):
        """
        Возвращает площадь фигуры. Это абстрактный класс. 
        Из него будут наследоваться классы круга и треугольника.
        """
        pass

class Circle(Shape):
    """
    Класс для круга.
    """
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return circle_area(self.radius)

class Triangle(Shape):
    """
    Класс для треугольника.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        return triangle_area(self.a, self.b, self.c)
    
    def is_right(self):
        return is_right_triangle(self.a, self.b, self.c)

def get_area(shape):
    """
    Вычисляет площадь фигуры, принимая объект фигуры как аргумент.
    """
    return shape.area()