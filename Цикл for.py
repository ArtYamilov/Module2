# for i in 1, 2, 3, 4:  # i,j,k - переменные для цикла, переменная существует только в пределах цикла.
#     print('ok')
# # for - цикл повторений в количестве от переменных.
# for i in 1, 2, 3, 4:  # после in задается последовательность которая является итерабельной - переменные,
#     # значения которые можно перебрать.
#     print(i)
#
# for i in 'Hello':
#     print(i)
#
# list_ = ['one', 'two', 'three']
# for i in list_:
#     print(i)
#
# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
# print(list_)
#
# list_ = ['one', 'two', 'three']
# for i in range(5):  # 0, 1, 2, 3, 4.
#     print(i)
#
# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):  # 0, 1, 2.
#     print(i)
#
# list_ = ['one', 'two', 'three']
# for i in range(len(list_)):  # 0, 1, 2.
#     list_[i] = ':)'
# print(list_)

# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):  # 0, 1, 2.
#     sum_ += list_2[i]
# print(sum_)

# for i in range(1, 11, 2):  # i -1; (start, stop, step.)
#     print(i)
#
# for i in range(1, 11):  # таблица умножения.
#     for j in range(1, 11):  # j - 1, 2, 3, 4...; крайняя цифра из последовательности,
#         # а именно 11 не включается в последовательность.
#         print(f'{i} x {j} = {i * j}')  # f - используется, чтобы напечатать переменную со строкой в одном операторе
#         # print, в фигурных скобках указывается переменная.
#
# dict_ = {'a': 1, 'b': 2, 'c': 3}
#
# for i in dict_:
#     print(i, dict_[i])  # i - сохраняет в себе значение ключа, dict_[i] - передает значение ключа.

# dict_ = {'a': 1, 'b': 2, 'c': 3}
#
# for i, k in dict_.items():  # в цикле for можно создавать несколько переменных используя различные методы,
#     # например .items
#     print(i, k)
#
# Домашнее задание.

my_cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in my_cars:
    print('Я езжу на автомобиле марки', i, cars_count)
    cars_count += 10
