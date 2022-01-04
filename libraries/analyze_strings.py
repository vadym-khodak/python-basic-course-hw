"""
Написати функцію, яка приймає три аргументи text, num_of_chars, is_most_common (str, int, bool). Де:
- text, будь який рядок з текстом;
- num_of_chars, кількість найбільш/найменш популярних символів у рядку;
- is_most_common, не обов'язковий, за замовчуванням дорівнює True.
Якщо is_most_common дорівнює True - повернути список з найбільш популярних символів, якщо is_most_common дорівнює False - повернути список з найменш популярних. Довжина списку не має бути більше ніж num_of_chars. Символи мають бути відсортовані у залежності від кількості повторень, якщо декілька символів повторюються однакову кількість разів - то вони мають йти в алфавітному порядку.
>>> analyze_chars('Hello amazing World', 3)
['l', 'a', 'o']
>>> analyze_chars('Hello amazing World', 0)
[]
>>> analyze_chars('Hello amazing World', 0, is_most_common=False)
[]
>>> analyze_chars('Hello', 2)
['l', 'e']
>>> analyze_chars('Hi', 3)
['h', 'i']
>>> analyze_chars('Hi', 1)
['h']
>>> analyze_chars('Hi', 1, is_most_common=False)
['h']

"""
from collections import Counter


def analyze_chars(text: str, num_of_chars, is_most_common=True):
    chars = []
    for char in text.lower():
        if char.isalpha():
            chars.append(char)
    chars.sort()
    if not is_most_common:
        chars.reverse()
    prepared_text = "".join(chars)
    counter = Counter(prepared_text)
    common = counter.most_common()
    if not is_most_common:
        common.reverse()
    result = []
    for char, _ in common:
        result.append(char)
    return result[:num_of_chars]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
