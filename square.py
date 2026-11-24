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
        self.assertEqual(area(7), 49)

    def test_per_mul(self):
        self.assertEqual(perimeter(14), 56)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_per_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(0.5), 0.25)

    def test_per_float(self):
        self.assertAlmostEqual(perimeter(0.5), 2.0)

    def test_area_large(self):
        self.assertEqual(area(10**6), 10**12)