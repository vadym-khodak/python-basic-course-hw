"""
Написати програму яка буде питати користувача ввести
ім'я та друкуватиме у терміналі "Привіт <введене ім'я>"
"""

name = input("Could you please enter your name? \n")

print("Hello", name)
print("Hello " + name)
print("Hello %s" % name)
print("Hello {}".format(name))
print("Hello {name}".format(name=name))
print(f"Hello {name}")

