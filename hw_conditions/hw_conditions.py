"""
Звичайний рівень (Хто що п’є):
Написати програму яка буде питати вік у користувача та в залежності від віку
буде друкувати до якої групи відноситься цей вік та що може випити у цьому віці.

вік менше 14 - діти (п’ють молоко)
вік менше 18 - тінейджери  (п’ють кока-колу)
вік менше 21 - молодь  (п’ють пиво)
вік більше 21 - дорослі  (п’ють віскі)
"""

# Варіант обробки введення значення користувачем
# INPUT_ERROR_MESSAGE = "Помилка: введіть будь-ласка ціле число, яке більше або дорівнює 0"
# while True:
#     try:
#         user_age = int(input("Введіть будь ласка скільки Вам років: "))
#         if user_age < 0:
#             print(INPUT_ERROR_MESSAGE)
#             continue
#     except ValueError:
#         print(INPUT_ERROR_MESSAGE)
#     else:
#         break

user_age = int(input("Введіть будь ласка скільки Вам років: "))

if user_age < 14:
    phrase = "діти (п’ють молоко)"
elif user_age < 18:
    phrase = "тінейджери  (п’ють кока-колу)"
elif user_age < 21:
    phrase = "молодь  (п’ють пиво)"
else:
    phrase = "дорослі  (п’ють віскі)"


if __name__ == "__main__":
    print(phrase)


