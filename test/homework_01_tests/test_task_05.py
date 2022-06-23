import unittest
from homework_01.dz_01 import count_find_num


class Task05TestCase(unittest.TestCase):
    """Тесты для проверки задачи №5 из ДЗ №1."""

    def test_count_find_num_01(self):
        primes_l = [2, 5, 7]
        limit = 500
        result = count_find_num(primes_l, limit)
        self.assertEqual(result, [5, 490])

    def test_count_find_num_02(self):
        primes_l = [2, 3]
        limit = 200
        result = count_find_num(primes_l, limit)
        self.assertEqual(result, [13, 192])

    def test_count_find_num_03(self):
        primes_l = [2, 5]
        limit = 200
        result = count_find_num(primes_l, limit)
        self.assertEqual(result, [8, 200])

    def test_count_find_num_04(self):
        primes_l = [2, 3, 5]
        limit = 500
        result = count_find_num(primes_l, limit)
        self.assertEqual(result, [12, 480])

    def test_count_find_num_05(self):
        primes_l = [2, 3, 47]
        limit = 200
        result = count_find_num(primes_l, limit)
        self.assertEqual(result, [])
