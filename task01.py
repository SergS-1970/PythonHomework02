# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

number = input('Введите число: ')
sumOfDigits = 0
for a in number:
    if a.isdigit():
        sumOfDigits += int(a)

print(f"Сумма цифр в числе: {number} равна:", sumOfDigits)