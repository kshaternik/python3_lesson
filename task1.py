# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. Пример:

# [5, 7, 4, 8, 2]

list = [5, 7, 4, 8, 2]

print(list)

sum = 0
for i in range(len(list)):
    if i %  2 != 0:
        sum = sum + list[i]
print(f'Sum of elements in odd position {list} is', sum)