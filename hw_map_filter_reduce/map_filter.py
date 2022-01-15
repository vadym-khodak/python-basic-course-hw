"""
Написати функцію, яка приймає послідовність повних імен та повертає
ту саму послідовність імен, де всі імена та прізвища починаються з великих літер,
а решта літер маленькі та відсутні зайві пробіли з початку та в кінці повного ім’я
та лишає тільки один пробіл між ім’ям та прізвищем. Використовувати map() та filter().

Приклад:
>>> format_names([" joHn    DOE  ", " BRIan    smiTh  "])
['John Doe', 'Brian Smith']
"""


def format_names(names):
    return list(map(lambda name: " ".join(filter(lambda i: i, name.strip().title().split(" "))), names))


print(format_names([" joHn     DOE  ", " BRIan     smiTh  "]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
