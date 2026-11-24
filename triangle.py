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
        self.assertEqual(area(10, 10), 50)

    def test_perimeter_mul(self):
        self.assertEqual(perimeter(5, 10, 15), 30)

    def test_area_zero_base(self):
        self.assertEqual(area(0, 10), 0)

    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 5.0)

    def test_per_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_per_float(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.0), 7.0)

    def test_area_large(self):
        self.assertEqual(area(10**6, 10**6), 5 * 10**11)