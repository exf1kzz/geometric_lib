import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника со сторонами a и b.

        Args:
            a (int): десятичное целое число
            b (int): десятичное целое число

        Returns:
            int: площадь прямоугольника, вычисляемая по формуле a * b

        Example:
            print(area(5, 3)) # Вывод: 15
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника со сторонами a и b.

        Args:
            a (int): десятичное целое число
            b (int): десятичное целое число

        Returns:
            int: периметр прямоугольника, вычисляемый по формуле (a + b) * 2

        Example:
            print(perimeter(5, 3)) # Вывод: 16
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = area(5.5, 3.2)
        self.assertEqual(res, 17.6)

    def test_float_perimeter(self):
        res = perimeter(5.5, 3.2)
        self.assertEqual(res, 17.4)

    def test_string_to_int_area(self):
        res = area(int("10"), int("5"))
        self.assertEqual(res, 50)

    def test_string_to_int_perimeter(self):
        res = perimeter(int("10"), int("5"))
        self.assertEqual(res, 30)

    def test_string_to_float_area(self):
        res = area(float("5.5"), float("3.2"))
        self.assertEqual(res, 17.6)

    def test_string_to_float_perimeter(self):
        res = perimeter(float("5.5"), float("3.2"))
        self.assertEqual(res, 17.4)

        
