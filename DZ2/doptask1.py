'''Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.'''


number = int(input('Введите размер списка '))
list = []
sum = 0
for i in range(number):

    if i % 2 != 0:
        sum += list[i]
print(list)


print(len(number))
