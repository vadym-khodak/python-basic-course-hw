"""
Написати програму яка буде питати користувача ввести два
числа та друкуватиме у терміналі суму та різницю цих чисел
"""
first_number = int(input("Could you please enter the first number? \n"))
second_number = int(input("Could you please enter the second one? \n"))

numbers_sum = first_number + second_number
print("Sum of those numbers is {}".format(numbers_sum))

numbers_substraction = first_number - second_number
print(f"Substraction of those numbers is {numbers_substraction}")
