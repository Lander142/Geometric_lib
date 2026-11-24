import unittest

def area(a, h):
    '''
    Возвращает площадь треугольника по стороне и высоте, проведенной к ней.

        Параметры:
            a (int | float): длина основания треугольника
            h (int | float): высота, проведенная к основанию

        Возвращаемое значение:
            float: площадь треугольника

        Пример вызова:
            area(4, 5) -> 10.0
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника по трем сторонам.

        Параметры:
            a (int | float): длина первой стороны
            b (int | float): длина второй стороны
            c (int | float): длина третьей стороны

        Возвращаемое значение:
            int | float: периметр треугольника

        Пример вызова:
            perimeter(3, 4, 5) -> 12
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_perimeter_mul(self):
        res = perimeter(5, 10, 15)
        self.assertEqual(res, 30)