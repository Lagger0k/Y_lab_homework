import unittest
from homework_01.dz_01 import zeros


class Task03TestCase(unittest.TestCase):
    """Тесты для проверки задачи №3 из ДЗ №1."""

    def test_zeros_01(self):
        number = 6
        result = zeros(number)
        self.assertEqual(result, 1)

    def test_zeros_02(self):
        number = 12
        result = zeros(number)
        self.assertEqual(result, 2)

    def test_zeros_03(self):
        number = 0
        result = zeros(number)
        self.assertEqual(result, 0)

    def test_zeros_04(self):
        number = 30
        result = zeros(number)
        self.assertEqual(result, 7)

