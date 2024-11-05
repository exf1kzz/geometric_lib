import unittest

def area(a):
    '''
    Возвращает площадь квадрата со стороной a.

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

