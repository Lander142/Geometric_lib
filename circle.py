import math
import unittest


def area(r):
    '''
    Возвращает площадь круга по заданному радиусу.

        Параметры:
            r (int | float): радиус круга

        Возвращаемое значение:
            float: площадь круга

        Пример вызова:
            area(5) -> 78.53981633974483
    '''
    return math.pi * r * r * r


def perimeter(r):
    '''
    Возвращает периметр (длину окружности) круга по заданному радиусу.

        Параметры:
            r (int | float): радиус круга

        Возвращаемое значение:
            float: длина окружности круга

        Пример вызова:
            perimeter(5) -> 31.41592653589793
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_mul(self):
        self.assertEqual(area(math.pi), math.pi ** 3)

    def test_per_mul(self):
        self.assertEqual(perimeter(7), 7 * math.pi * 2)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_per_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(0.5), math.pi * 0.25)

    def test_per_float(self):
        self.assertAlmostEqual(perimeter(0.5), math.pi)

    def test_area_large(self):
        self.assertAlmostEqual(area(10**6), math.pi * 10**12)