# Назовите файл `test_count_vowels.py`

import pytest  # Импортируем pytest

# 1) Функция для подсчета гласных в строке
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"  # Определяем гласные буквы (как строчные, так и заглавные)
    return sum(1 for char in s if char in vowels)  # Считаем количество гласных в строке

# 2) Написание тестов с использованием pytest

# Тест 1: Проверяем строку, содержащую только гласные
def test_all_vowels():
    assert count_vowels("aeiou") == 5  # 5 строчных гласных
    assert count_vowels("AEIOU") == 5  # 5 заглавных гласных

# Тест 2: Проверяем строку, не содержащую гласных
def test_no_vowels():
    assert count_vowels("bcdfg") == 0  # Ни одной гласной
    assert count_vowels("BCDFG") == 0  # Ни одной гласной

# Тест 3: Проверяем строку со смешанными символами
def test_mixed_string():
    assert count_vowels("Hello World") == 3  # В слове "Hello World" три гласные: 'e', 'o', 'o'
    assert count_vowels("PyTest") == 1  # В слове "PyTest" одна гласная: 'e'
    assert count_vowels("AeiOu") == 5  # Все гласные присутствуют
    assert count_vowels("abcdefg") == 2  # В слове "abcdefg" две гласные: 'a', 'e'

# Дополнительный тест: Использование pytest.mark.parametrize для проверки нескольких случаев одновременно
@pytest.mark.parametrize("input_str, expected_count", [
    ("aeiouAEIOU", 10),
    ("Python", 1),
    ("", 0),
    ("bcdfghjklmnpqrstvwxyz", 0),
    ("Beautiful Day", 6)
])
def test_various_cases(input_str, expected_count):
    assert count_vowels(input_str) == expected_count
