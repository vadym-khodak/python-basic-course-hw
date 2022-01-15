"""
Звичайний рівень (Сума факторіалів):
Написати функцію, яка приймає число “n” типу int та повертає
суму факторіалів всіх чисел від 1 до “n”. Використовувати reduce().


Приклад:
>>> factorial_sum(4)
33
>>> factorial_sum(10)
4037913

"""
from functools import reduce


def factorial_sum(n: int) -> int:
    factorials = []
    for i in range(1, n + 1):
        factorials.append(reduce(lambda x, y: x * y, range(1, i + 1)))
    return reduce(lambda x, y: x + y, factorials)


print(factorial_sum(100))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
