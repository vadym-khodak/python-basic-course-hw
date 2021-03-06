"""
Ускладнений рівень (Калькулятор пального):

Написати програму, яка питає в користувача ввести кількість галонів та ціну за галон у доларах.

При покупці 2 і більше галонів надається знижка в розмірі 5 центів за галон, при покупці 4 і
більше галонів – знижка в розмірі 10 центів за галон і так далі кожні два літри, до максимальної
знижки 25 центів за галонів. Надрукуйте в консолі загальну вартість, округлену до 2 знаків після коми.

"""

amount = float(input("Введіть кількість галонів для заправки - "))
price = float(input("Введіть суму за один галон в долларах США - "))


if amount < 2:
    total_cost = amount * price
elif amount < 4:
    total_cost = amount * (price - 0.05)
elif amount < 6:
    total_cost = amount * (price - 0.1)
elif amount < 8:
    total_cost = amount * (price - 0.15)
elif amount < 10:
    total_cost = amount * (price - 0.2)
else:
    total_cost = amount * (price - 0.25)

print(f'Загальна вартість: {round(total_cost, 2)} центів.')


if __name__ == "__main__":
    pass


