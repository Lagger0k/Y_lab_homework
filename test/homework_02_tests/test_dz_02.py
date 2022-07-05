import unittest
from homework_02.dz_02_01 import _calculates_the_distance_between_points, main, Point


class Dz02TestCase(unittest.TestCase):

    def test__calculates_the_distance_between_points(self):
        point_1 = Point(0, 2)
        point_2 = Point(2, 5)
        result = _calculates_the_distance_between_points(point_1, point_2)
        self.assertEqual(result, 3.605551275463989)

    def test_main(self):
        post_office = Point(0, 2)
        points = [Point(2, 5), Point(6, 6), Point(5, 2), Point(8, 3)]
        result = main(post_office, points)
        self.assertEqual(result,
                         '(0, 2) -> (2, 5)[3.605551275463989] -> (6, 6)[4.123105625617661] -> (8, 3)[3.605551275463989]'
                         ' -> (5, 2)[3.1622776601683795] -> (0, 2)[5.0] = 19.49648583671402')
