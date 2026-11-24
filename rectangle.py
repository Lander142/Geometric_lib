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
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)