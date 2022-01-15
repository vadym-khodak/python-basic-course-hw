"""
Написати функцію, яка приймає два аргументи типу int що відповідають проміжку часу початкового року
до кінцевого року включно та повертає список (list) рядків (str), де кожний рядок представлений
датою п’ятниці 13-го. Функція має обробляти неправильні типи даних для аргументів функції та друкувати
в консолі повідомлення про це. Посилання на таблицю кодів форматування дати.


Приклад:
>>> friday_thirteenth(2021, 2022)
['13 Aug 21', '13 May 22']

"""
from datetime import date


def friday_thirteenth(start_year, end_year):
    """
    >>> friday_thirteenth(1999, 2000)
    ['13 Aug 99', '13 Oct 00']
    >>> friday_thirteenth(2014, 2015)
    ['13 Jun 14', '13 Feb 15', '13 Mar 15', '13 Nov 15']
    >>> friday_thirteenth(2018, 2018)
    ['13 Apr 18', '13 Jul 18']
    >>> friday_thirteenth(2019, 2018)
    []
    >>> friday_thirteenth(2021, 2022)
    ['13 Aug 21', '13 May 22']
    """
    # Get range of years to check
    results = []
    for year in range(start_year, end_year + 1):
        # Get 13 day of each month and check whether it is Friday or not
        for month in range(1, 13):
            maybe_friday = date(year, month, 13)
            if maybe_friday.isoweekday() == 5:
                # If True add to results
                results.append(maybe_friday.strftime("%d %b %y"))
    return results


if __name__ == '__main__':
    import doctest
    doctest.testmod()
