import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def dimention(self):
        pass

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    @abstractmethod
    def volume(self):
        pass

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return "2D"

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0.0
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimention(self):
        return "2D"

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        try:
            s = (self.c + self.d - abs(self.a - self.b)) / 2
            h = 2 / abs(self.a - self.b) * math.sqrt(
                s * (s - self.c) * (s - self.d) * (s - self.a + self.b))
            return 0.5 * (self.a + self.b) * h
        except:
            return 0.0

    def volume(self):
        return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return "2D"

    def perimetr(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def volume(self):
        return self.square()

class Ball(Circle):
    def dimention(self):
        return "3D"

    def volume(self):
        return 4 / 3 * math.pi * self.r ** 3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return 1 / 3 * self.squareBase() * self.h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return 1 / 3 * self.squareBase() * self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return "3D"

    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return "3D"

    def height(self):
        return self.h

    def volume(self):
        return 1 / 3 * super().square() * self.h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return "3D"

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h

def parse(line):
    tokens = line.strip().split()
    name, args = tokens[0], list(map(float, tokens[1:]))
    if name == "Triangle": return Triangle(*args)
    if name == "Rectangle": return Rectangle(*args)
    if name == "Trapeze": return Trapeze(*args)
    if name == "Parallelogram": return Parallelogram(*args)
    if name == "Circle": return Circle(*args)
    if name == "Ball": return Ball(*args)
    if name == "TriangularPyramid": return TriangularPyramid(*args)
    if name == "QuadrangularPyramid": return QuadrangularPyramid(*args)
    if name == "RectangularParallelepiped": return RectangularParallelepiped(*args)
    if name == "Cone": return Cone(*args)
    if name == "TriangularPrism": return TriangularPrism(*args)
    return None

def main():
    filepaths = ["input01.txt", "input02.txt", "input03.txt"]
    figures = []

    for path in filepaths:
        with open(path, 'r') as f:
            for line in f:
                fig = parse(line)
                if fig: figures.append((line.strip(), fig))

    max_figure = max(figures, key=lambda item: item[1].volume())

    with open("output_demo.txt", "w", encoding="utf-8") as f:
        f.write("Фігура з найбільшою мірою (площа або об'єм):\n")
        f.write(f"{max_figure[0]}\n")
        f.write(f"Міра (volume): {max_figure[1].volume():.2f}\n")

if __name__ == "__main__":
    main()
