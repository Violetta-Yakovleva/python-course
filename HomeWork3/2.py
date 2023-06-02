# Задача 2. Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

# n = int(input('Введите кол-во элементов списка: '))
# list_A = []
# for _ in range(n):
#     list_A.append(int(input('Введите значения списка: ')))
#
# x = int(input('Введите число для поиска ближайшего числа: '))
# near_x = list_A[0]
# diff_0 = abs(x - near_x)
# i = 0
# while i < len(list_A):
#     diff = abs(x - list_A[i])
#     if diff < diff_0:
#         diff_0 = diff
#         near_x = list_A[i]
#     i += 1
#
# print(list_A)
# print(f'Наиболее близкое число к заданному: {near_x}')


# (*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X,
# выводим все числа в отсортированном виде (по возрастанию)

# n = int(input('Введите кол-во элементов списка: '))
# list_A = []
# for _ in range(n):
#     list_A.append(int(input('Введите значения списка: ')))
#
# x = int(input('Введите число для поиска ближайшего(-их) числа(-ел): '))

list_A = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = 9

near_x = list_A[0]
diff_0 = abs(x - near_x)
i = 0
list_B = []

while i < len(list_A):
    diff = abs(x - list_A[i])
    if diff < diff_0:
        diff_0 = diff
        list_B.append(diff_0)
    i += 1

print(list_A)
print(list_B)
