import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import unittest
import circle
import reactangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = circle.area(5)
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, places=7)
        
    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = circle.area(5.5)
        self.assertAlmostEqual(res, 95.03317777109124, places=7)

    def test_float_perimeter(self):
        res = circle.perimeter(5.5)
        self.assertAlmostEqual(res, 34.55751918948773, places=7)

    def test_string_to_int_area(self):
        res = circle.area(int("5"))
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_string_to_int_perimeter(self):
        res = circle.perimeter(int("5"))
        self.assertAlmostEqual(res, 31.41592653589793, places=7)

    def test_string_to_float_area(self):
        res = circle.area(float("5.5"))
        self.assertAlmostEqual(res, 95.03317777109124, places=7)

    def test_string_to_float_perimeter(self):
        res = circle.perimeter(float("5.5"))
        self.assertAlmostEqual(res, 34.55751918948773, places=7)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = reactangle.area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = reactangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_square_perimeter(self):
        res = reactangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_zero_perimeter(self):
        res = reactangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = reactangle.area(5.5, 3.2)
        self.assertEqual(res, 17.6)

    def test_float_perimeter(self):
        res = reactangle.perimeter(5.5, 3.2)
        self.assertEqual(res, 17.4)

    def test_string_to_int_area(self):
        res = reactangle.area(int("10"), int("5"))
        self.assertEqual(res, 50)

    def test_string_to_int_perimeter(self):
        res = reactangle.perimeter(int("10"), int("5"))
        self.assertEqual(res, 30)

    def test_string_to_float_area(self):
        res = reactangle.area(float("5.5"), float("3.2"))
        self.assertEqual(res, 17.6)

    def test_string_to_float_perimeter(self):
        res = reactangle.perimeter(float("5.5"), float("3.2"))
        self.assertEqual(res, 17.4)

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = square.perimeter(20)
        self.assertEqual(res, 80)
        
    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_float_area(self):
        res = square.area(5.5)
        self.assertEqual(res, 30.25)

    def test_float_perimeter(self):
        res = square.perimeter(5.5)
        self.assertEqual(res, 22)

    def test_string_to_int_area(self):
        res = square.area(int("10"))
        self.assertEqual(res, 100)

    def test_string_to_int_perimeter(self):
        res = square.perimeter(int("20"))
        self.assertEqual(res, 80)

    def test_string_to_float_area(self):
        res = square.area(float("5.5"))
        self.assertEqual(res, 30.25)

    def test_string_to_float_perimeter(self):
        res = square.perimeter(float("5.5"))
        self.assertEqual(res, 22)

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = triangle.area(15, 4)
        self.assertEqual(res, 30)

    def test_perimeter(self):
        res = triangle.perimeter(5, 10, 6)
        self.assertEqual(res, 21)
        
    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 1)
        self.assertEqual(res, 1)

    def test_float_area(self):
        res = triangle.area(5.5, 4.5)
        self.assertEqual(res, 12.375)

    def test_float_perimeter(self):
        res = triangle.perimeter(5.5, 4.5, 3.5)
        self.assertEqual(res, 13.5)

    def test_string_to_int_area(self):
        res = triangle.area(int("15"), int("4"))
        self.assertEqual(res, 30)

    def test_string_to_int_perimeter(self):
        res = triangle.perimeter(int("5"), int("10"), int("6"))
        self.assertEqual(res, 21)

    def test_string_to_float_area(self):
        res = triangle.area(float("5.5"), float("4.5"))
        self.assertEqual(res, 12.375)

    def test_string_to_float_perimeter(self):
        res = triangle.perimeter(float("5.5"), float("4.5"), float("3.5"))
        self.assertEqual(res, 13.5)


if __name__ == "__main__":
    unittest.main()
