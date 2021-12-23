"""
Ускладнений рівень (Числа Фібоначчі):
Написати функцію яка приймає один аргумент типу int, який за замовчуванням має
значення 123456 та повертає послідовність чисел Фібоначчі які менші за передане число.

Примітка:
- тут ви можете знайти інформацію про те що таке послідовність Фібоначчі
https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D0%BB%D1%96%D0%B4%D0%BE%D0%B2%D0%BD%D1%96%D1%81%D1%82%D1%8C_%D0%A4%D1%96%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D1%96
"""


def fibonacci_sequence(number=123456):
    sequence = [1, 1]
    if number <= 1:
        return []
    while True:
        fib = sequence[-2] + sequence[-1]
        if fib >= number:
            break
        sequence.append(fib)
    return sequence


if __name__ == "__main__":
    assert len(fibonacci_sequence()) == 26
    assert fibonacci_sequence(5) == [1, 1, 2, 3]
    assert fibonacci_sequence(10) == [1, 1, 2, 3, 5, 8]
