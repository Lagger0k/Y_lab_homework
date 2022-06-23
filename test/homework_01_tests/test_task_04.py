import unittest
from homework_01.dz_01 import bananas


class Task04TestCase(unittest.TestCase):
    """Тесты для проверки задачи №4 из ДЗ №1."""

    def test_bananas_01(self):
        input_string = "banann"
        result = bananas(input_string)
        self.assertEqual(result, set())

    def test_bananas_02(self):
        input_string = "banana"
        result = bananas(input_string)
        self.assertEqual(result, {"banana"})

    def test_bananas_03(self):
        input_string = "bbananana"
        result = bananas(input_string)
        self.assertEqual(result, {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                  "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                  "-ban--ana", "b-anana--"})

    def test_bananas_04(self):
        input_string = "bananaaa"
        result = bananas(input_string)
        self.assertEqual(result, {"banan-a-", "banana--", "banan--a"})

    def test_bananas_05(self):
        input_string = "bananana"
        result = bananas(input_string)
        self.assertEqual(result, {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"})
