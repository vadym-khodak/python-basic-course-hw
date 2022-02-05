"""
Написати клас Calculator, який має методи add, subtract, multiply, divide. 
Кожен з яких приймає два аргументи та повертає результат математичної дії. 
Класс Calculator має обраховувати кількість математичних операцій, 
які були проведені кожним екземпляром класу окремо та мати 
додатковий метод для виведення у консоль цієї кількості
Приклад:
calc = Calculator()
calc.add(2, 3)
5
calc.subtract(10, 4.5)
5.5
calc.print_operations_counter()
2
"""


class Calculator:
    def __init__(self):
        self.__counter = 0
    
    def add(self, a, b):
        self.__counter += 1
        return a + b
    
    def subtract(self, a, b):
        self.__counter += 1
        return a - b
    
    def multiply(self, a, b):
        self.__counter += 1
        return a * b
    
    def divide(self, a, b):
        self.__counter += 1
        return a / b
    
    def print_operations_counter(self):
        print(self.__counter)


if __name__ == "__main__":
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(10, 4.5) == 5.5
    calc.print_operations_counter()
