import unittest

def area(a):
    '''
    Возвращает площадь квадрата по заданной стороне.

        Параметры:
            a (int | float): длина стороны квадрата

        Возвращаемое значение:
            int | float: площадь квадрата

        Пример вызова:
            area(5) -> 25
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата по заданной стороне.

        Параметры:
            a (int | float): длина стороны квадрата

        Возвращаемое значение:
            int | float: периметр квадрата

        Пример вызова:
            perimeter(5) -> 20
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area_mul(self):
        res = area(7)
        self.assertEqual(res, 49)
    def test_per_mul(self):
        res = perimeter(14)
        self.assertEqual(res, 56)