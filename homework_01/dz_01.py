import ipaddress
import itertools
from functools import reduce


def domain_name(url: str) -> str:
    """Задача № 1. Функция находит доменное имя из строки с адресом"""
    if url.startswith('http'):
        end_of_url = url.split('//')[1]
        return domain_name(end_of_url)
    elif url.startswith('www'):
        domain = url.split('.')[1]
        return domain
    else:
        domain = url.split('.')[0]
        return domain


def int32_to_ip(int32: int) -> str:
    """Задача № 2. Функция принимает на вход 32-битное целое число
    (integer) и возвращает строковое представление его в виде IPv4-адреса:"""
    return ipaddress.ip_address(int32).__str__()


def zeros(number: int) -> int:
    """Задача № 3. Функция принимает на вход целое число (integer) и
    возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:"""
    count = 0
    while number >= 5:
        number //= 5
        count += number
    return count


def bananas(word: str) -> set:
    """Задача № 4. Функция принимает на вход строку и возвращает количество слов «banana» в строке.
    (Используйте - для обозначения зачеркнутой буквы)"""
    result = set()
    for combinations in itertools.combinations(range(len(word)), len(word) - 6):
        list_from_word = list(word)

        for i in combinations:
            list_from_word[i] = '-'
        variant = ''.join(list_from_word)

        if variant.replace('-', '') == 'banana':
            result.add(variant)
    return result


def count_find_num(primes_l: list, limit: int) -> list:
    """Задача № 5. Функция принимает на вход список простых множителей (primes_l) и целое число,
    предел (limit), после чего генерирует по порядку все числа.
    Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL."""
    base_number = reduce((lambda a, b: a * b), primes_l, 1)
    if base_number > limit:
        return []
    nums = [base_number]
    for i in primes_l:
        for n in nums:
            num = n * i
            while (num <= limit) and (num not in nums):
                nums.append(num)
                num *= i
    return [len(nums), max(nums)]
