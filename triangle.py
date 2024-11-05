import unittest

def area(a, h): 
    '''
    Возвращает площадь треугольника со стороной a и высотой h.

        Args:
            a (int): десятичное целое число
            h (int): десятичное целое число

        Returns:
            float: площадь треугольника, вычисляемая по формуле a * h / 2

        Example:
            print(area(5, 5)) # Вывод: 12.5
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника со сторонами a, b и c.

        Args:
            a (int): десятичное целое число
            b (int): десятичное целое число
            c (int): десятичное целое число

        Returns:
            int: периметр треугольника, вычисляемый по формуле a + b + c

        Example:
            print(perimeter(5, 5, 5)) # Вывод: 15
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = area(15, 4)
        self.assertEqual(res, 30)

    def test_perimeter(self):
        res = perimeter(5, 10, 6)
        self.assertEqual(res, 21)
        
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 1)
        self.assertEqual(res, 1)

