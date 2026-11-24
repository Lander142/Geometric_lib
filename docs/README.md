# Geometric Lib

Библиотека на Python для вычисления площади и периметра плоских геометрических фигур.

## Модули и функции

| Модуль | Функция | Описание | Формула |
| :--- | :--- | :--- | :--- |
| `circle.py` | `area(r)` | Площадь круга | π · r² |
| `circle.py` | `perimeter(r)` | Длина окружности | 2 · π · r |
| `rectangle.py` | `area(a, b)` | Площадь прямоугольника | a · b |
| `rectangle.py` | `perimeter(a, b)` | Периметр прямоугольника | 2 · (a + b) |
| `square.py` | `area(a)` | Площадь квадрата | a² |
| `square.py` | `perimeter(a)` | Периметр квадрата | 4 · a |
| `triangle.py` | `area(a, h)` | Площадь треугольника | a · h / 2 |
| `triangle.py` | `perimeter(a, b, c)` | Периметр треугольника | a + b + c |

## Пример использования

```python
import circle
import rectangle
import square
import triangle

# Круг
print(circle.area(5))             # 78.53981633974483
print(circle.perimeter(5))        # 31.41592653589793

# Прямоугольник
print(rectangle.area(3, 4))       # 12
print(rectangle.perimeter(3, 4))  # 14

# Квадрат
print(square.area(5))             # 25
print(square.perimeter(5))        # 20

# Треугольник
print(triangle.area(4, 5))        # 10.0
print(triangle.perimeter(3, 4, 5))# 12
```

## Запуск тестов

```bash
python -m unittest circle.py rectangle.py square.py triangle.py
```

## История изменений

* `7121dd36c8338e7df506fdfe15086171f6503d8e` — Add rectangle.py
* `5d7f960e8ac5326b97c305eba9c99ed634d65cc2` — fix bug in calculation for rectangle
* `c615fe22af45316b736530fe91cc451f3164a2fe` — new files
* `8f9fb03d923329c4afdaf8f2f067034b50e9bf26` — add tests