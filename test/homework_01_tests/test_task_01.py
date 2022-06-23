import unittest
from homework_01.dz_01 import domain_name


class Task01TestCase(unittest.TestCase):
    """Тесты для проверки задачи №1 из ДЗ №1."""

    def test_domain_name_01(self):
        domain = "http://google.com"
        result = domain_name(domain)
        self.assertEqual(result, "google")

    def test_domain_name_02(self):
        domain = "http://google.co.jp"
        result = domain_name(domain)
        self.assertEqual(result, "google")

    def test_domain_name_03(self):
        domain = "www.xakep.ru"
        result = domain_name(domain)
        self.assertEqual(result, "xakep")

    def test_domain_name_04(self):
        domain = "https://youtube.com"
        result = domain_name(domain)
        self.assertEqual(result, "youtube")

    def test_domain_name_05(self):
        domain = "http://github.com/carbonfive/raygun"
        result = domain_name(domain)
        self.assertEqual(result, "github")

    def test_domain_name_06(self):
        domain = "http://www.zombie-bites.com"
        result = domain_name(domain)
        self.assertEqual(result, "zombie-bites")

    def test_domain_name_07(self):
        domain = "https://www.cnet.com"
        result = domain_name(domain)
        self.assertEqual(result, "cnet")

