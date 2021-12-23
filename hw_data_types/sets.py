"""
Написати програму, яка буде питати користувача ввести будь-який рядок та друкуватиме
унікальні букви які використовувались у введеному рядку відсортовані за алфавітом
"""

some_text = input("Could you please enter some text? \n")

chars_set = set(some_text)

chars = sorted(chars_set)

chars_str = "".join(chars)
chars_str = chars_str.replace("\\", "")
chars_str = chars_str.replace("[", "")
chars_str = chars_str.replace("]", "")
chars_str = chars_str.replace("^", "")
chars_str = chars_str.replace("_", "")
chars_str = chars_str.replace("`", "")
chars_str = chars_str.strip(" .,/;:\"'{}=+-)(*&%$#@!~")
print(chars_str)
