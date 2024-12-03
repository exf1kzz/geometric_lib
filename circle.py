import math
import unittest

def area(r):
    '''	
	Возвращает площадь круга и мой коментарий 
	
		Параметры:
			r (int) : радиус круга
	
		Возвращаемое значение:
			float: площадь круга вычисляемая по формуле: math.pi * r * r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
	Возвращает периметр круга 
	
		Параметры:
			r (int) : радиус круга
	
		Возвращаемое значение:
			float: периметр круга вычисляемый по формуле: 2 * math.pi * r
    ''' 
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, places=7)
        
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = area(5.5)
        self.assertAlmostEqual(res, 95.03317777109124, places=7)

    def test_float_perimeter(self):
        res = perimeter(5.5)
        self.assertAlmostEqual(res, 34.55751918948773, places=7)

    def test_string_to_int_area(self):
        res = area(int("5"))
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_string_to_int_perimeter(self):
        res = perimeter(int("5"))
        self.assertAlmostEqual(res, 31.41592653589793, places=7)

    def test_string_to_float_area(self):
        res = area(float("5.5"))
        self.assertAlmostEqual(res, 95.03317777109124, places=7)

    def test_string_to_float_perimeter(self):
        res = perimeter(float("5.5"))
        self.assertAlmostEqual(res, 34.55751918948773, places=7)
