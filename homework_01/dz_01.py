import ipaddress
import itertools
import math


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
    factorial_from_number = math.factorial(number)
    count_zeros = len(str(factorial_from_number)) - len(str(factorial_from_number).rstrip('0'))
    return count_zeros


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
    valid_factors = []
    all_factors = []

    for number in range(2, limit+1):
        factors = []
        divisor = 2
        while divisor <= number:
            if number % divisor == 0:
                factors.append(divisor)
                number = number / divisor
            else:
                divisor += 1
        all_factors.append(factors)

    for factor in all_factors:
        if set(primes_l) == set(factor):
            valid_factors.append(factor)

    if valid_factors:
        iterations = len(valid_factors)
        max_number = max([math.prod(factor) for factor in valid_factors])
        return [iterations, max_number]
    else:
        return []
