"""
Написати програму яка буде питати користувача ввести послідовність імен розділених
комою та друкуватиме ту саму послідовність імен відсортовану за алфавітом
"""

names = input("Could you please enter some names separated by coma? \n")

split_names = names.replace(", ", ",").split(",")
split_names.sort()
sorted_names_string = ", ".join(split_names)
print(sorted_names_string)
