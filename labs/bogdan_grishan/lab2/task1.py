"""Дано ціле число. Якщо воно є додатним, то відняти від нього 8; в іншому разі не змінювати його.
Вивести отримане число."""

number = int(input("Введите целое число:"))

if number > 0:
    result = number - 8
    print("Результат:" + str(result))
else:
    print("Число не изменено:" + str(number))
