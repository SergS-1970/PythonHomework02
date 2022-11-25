# 5. Реализуйте алгоритм перемешивания списка.

from random import Random, randint

N = int(input('Введите число элементов '))
numbers = []

for i in range(N):
    numbers.append(randint(-N, N+1))
print(numbers)

def mixing(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list


print(mixing(numbers))
