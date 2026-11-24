import unittest


def area(a, b):
    '''
    Возвращает площадь прямоугольника по заданным сторонам.

        Параметры:
            a (int | float): длина первой стороны
            b (int | float): длина второй стороны

        Возвращаемое значение:
            int | float: площадь прямоугольника

        Пример вызова:
            area(3, 4) -> 12
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника по заданным сторонам.

        Параметры:
            a (int | float): длина первой стороны
            b (int | float): длина второй стороны

        Возвращаемое значение:
            int | float: периметр прямоугольника

        Пример вызова:
            perimeter(3, 4) -> 14
    '''
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(10, 0), 0)

    def test_both_zero_area(self):
        self.assertEqual(area(0, 0), 0)

    def test_square_mul(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)

    def test_area_large(self):
        self.assertEqual(area(10**6, 10**6), 10**12)

    def test_per_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_per_one_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_per_float(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)