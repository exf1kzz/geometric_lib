import unittest

def area(a):
    '''
    Возвращает площадь квадрата со стороной a. !!!тесты работать!!!))

        Args:
            a (int): десятичное целое число

        Returns:
            int: площадь квадрата, вычисляемая по формуле a * a

        Example:
            print(area(5)) # Вывод: 25
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата со стороной a.
    
        Args:
            a (int): десятичное целое число

        Returns:
            int: периметр квадрата, вычисляемый по формуле 4 * a

        Example:
            print(perimeter(5)) # Вывод: 20
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = perimeter(20)
        self.assertEqual(res, 80)
        
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = area(5.5)
        self.assertEqual(res, 30.25)

    def test_float_perimeter(self):
        res = perimeter(5.5)
        self.assertEqual(res, 22)

    def test_string_to_int_area(self):
        res = area(int("10"))
        self.assertEqual(res, 100)

    def test_string_to_int_perimeter(self):
        res = perimeter(int("20"))
        self.assertEqual(res, 80)

    def test_string_to_float_area(self):
        res = area(float("5.5"))
        self.assertEqual(res, 30.25)

    def test_string_to_float_perimeter(self):
        res = perimeter(float("5.5"))
        self.assertEqual(res, 22)

