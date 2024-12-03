import unittest
import circle
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_area1(self):
        res = rectangle.area(1, 5)
        self.assertEqual(res, 5)

    def test_area2(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area3(self):
        res = rectangle.area(100, 100)
        self.assertEqual(res, 10000)

    def test_area4(self):
        res = rectangle.area(12, 13)
        self.assertEqual(res, 156)

    def test_area5(self):
        res = rectangle.area(77, 83)
        self.assertEqual(res, 6391)

    def test_perimeter1(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter2(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter3(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter4(self):
        res = rectangle.perimeter(1000, 1000)
        self.assertEqual(res, 4000)

    def test_perimeter5(self):
        res = rectangle.perimeter(13, 12)
        self.assertEqual(res, 50)


class CircleTestCase(unittest.TestCase):
    def test_area1(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, 3.14, places=2)

    def test_area2(self):
        res = circle.area(10)
        self.assertAlmostEqual(res, 314.16, places=2)

    def test_area3(self):
        res = circle.area(100)
        self.assertAlmostEqual(res, 31415.93, places=2)

    def test_area4(self):
        res = circle.area(4)
        self.assertAlmostEqual(res, 50.27, places=2)

    def test_area5(self):
        res = circle.area(77)
        self.assertAlmostEqual(res, 18626.5, places=2)

    def test_perimeter1(self):
        res = circle.perimeter(12)
        self.assertAlmostEqual(res, 75.4, places=2)

    def test_perimeter2(self):
        res = circle.perimeter(45)
        self.assertAlmostEqual(res, 282.74, places=2)

    def test_perimeter3(self):
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.28, places=2)

    def test_perimeter4(self):
        res = circle.perimeter(77)
        self.assertAlmostEqual(res, 483.81, places=2)

    def test_perimeter5(self):
        res = circle.perimeter(89)
        self.assertAlmostEqual(res, 559.2, places=2)

class TriangleTestCase(unittest.TestCase):
    def test_area1(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_area2(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_area3(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_area4(self):
        res = triangle.area(7, 8)
        self.assertEqual(res, 28)

    def test_area5(self):
        res = triangle.area(15, 20)
        self.assertEqual(res, 150)

    def test_perimeter1(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter2(self):
        res = triangle.perimeter(6, 8, 10)
        self.assertEqual(res, 24)

    def test_perimeter3(self):
        res = triangle.perimeter(7, 7, 7)
        self.assertEqual(res, 21)

    def test_perimeter4(self):
        res = triangle.perimeter(5, 12, 13)
        self.assertEqual(res, 30)

    def test_perimeter5(self):
        res = triangle.perimeter(10, 15, 20)
        self.assertEqual(res, 45)


class SquareTestCase(unittest.TestCase):
    def test_area1(self):
        res = square.area(1)
        self.assertEqual(res, 1)

    def test_area2(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_area3(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_area4(self):
        res = square.area(20)
        self.assertEqual(res, 400)

    def test_area5(self):
        res = square.area(50)
        self.assertEqual(res, 2500)

    def test_perimeter1(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter2(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter3(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter4(self):
        res = square.perimeter(20)
        self.assertEqual(res, 80)

    def test_perimeter5(self):
        res = square.perimeter(50)
        self.assertEqual(res, 200)


if __name__ == "__main__":
    unittest.main()
