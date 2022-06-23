import unittest
from homework_01.dz_01 import int32_to_ip


class Task02TestCase(unittest.TestCase):
    """Тесты для проверки задачи №2 из ДЗ №1."""

    def test_int32_to_ip_01(self):
        int32 = 2149583361
        result = int32_to_ip(int32)
        self.assertEqual(result, "128.32.10.1")

    def test_int32_to_ip_02(self):
        int32 = 32
        result = int32_to_ip(int32)
        self.assertEqual(result, "0.0.0.32")

    def test_int32_to_ip_03(self):
        int32 = 0
        result = int32_to_ip(int32)
        self.assertEqual(result, "0.0.0.0")

    def test_int32_to_ip_04(self):
        int32 = 2154959208
        result = int32_to_ip(int32)
        self.assertEqual(result, "128.114.17.104")

    def test_int32_to_ip_05(self):
        int32 = 2149583361
        result = int32_to_ip(int32)
        self.assertEqual(result, "128.32.10.1")
