"""9.Мастям гральних карт присвоєно порядкові номери: 1 - піки, 2 - трефи, 3 - бубни, 4 - черви.
Вартості карт, які старші за десятку, привласнені номери: 11 - валет, 12 - дама, 13 - король, 14 - туз.
Дано два цілих числа: N - вартість (6 ≤ N ≤ 14) і M - масть карти (1 ≤ M ≤ 4).
Вивести назву відповідної карти виду «шістка бубон», «дама черв», «туз треф», тощо."""

N = int(input("Введіть вартість карти(від 6 до 14): "))
M = int(input("Введіть масть карти(від 1 до 4): "))

if N == 6:
    a = 'Шістка-'
elif N == 7:
    a = 'Сім-'
elif N == 8:
    a = 'Вісім-'
elif N == 9:
    a = "Дев'ять-"
elif N == 10:
    a = 'Десять-'
elif N == 11:
    a = 'Валет-'
elif N == 12:
    a = 'Дама-'
elif N == 13:
    a = 'Король-'
elif N == 14:
    a = 'Туз-'
elif N < 6 or N > 14:
    a = 'Введене невірне значення-'

if M == 1:
    b = 'пік'
elif M == 2:
    b = 'треф'
elif M == 3:
    b = 'бубон'
elif M == 4:
    b = 'черв'
elif M < 1 or M > 4:
    b = 'введене невірне значення'
print(a+b)