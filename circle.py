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
    return math.pi * r * r


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

class CirlceTestCase(unittest.TestCase):
    def test_area_mul(self):
        res = area(math.pi)
        self.assertEqual(res, math.pi**3)
    def test_per_mul(self):
        res = perimeter(7)
        self.assertEqual(res, 7 * math.pi * 2)