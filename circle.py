import math
import unittest

def area(r):
    '''	
	Возвращает площадь круга
	
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
