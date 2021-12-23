"""
Звичайний рівень (Середнє непарних чисел):
Написати функцію яка приймає необмежену кількість порядкових аргументів типу int, один
іменований аргумент типу list[int] та повертає середнє значення всіх непарних чисел
"""


def odds_avg(*args, numbers=None):
    if not numbers and not args:
        return "There is no any arguments. Please pass some numbers to the function"
    if not numbers:
        numbers = []
    numbers.extend(args)
    sum_ = 0
    count_odds = 0
    for num in numbers:
        if num % 2 != 0:
            sum_ += num
            count_odds += 1
    if sum_:
        return sum_ / count_odds
    else:
        return "There is no odd numbers"


if __name__ == "__main__":
    assert odds_avg() == "There is no any arguments. Please pass some numbers to the function"
    assert odds_avg(2, 4, numbers=[6, 8, 10]) == "There is no odd numbers"
    assert odds_avg(2, 4, numbers=[1, 3]) == 2
    assert odds_avg(2, 4, 5, numbers=[1, 3]) == 3
    assert odds_avg(numbers=[1, 3, 4, 6, 8, 5]) == 3
    assert odds_avg(2, 4, 5) == 5
