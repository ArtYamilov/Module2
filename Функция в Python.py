# # Обычная функция.
# def say_hello():  # define - определять, say_hello - имя функции.
#     print('Hello')  # обычная функция.
#
#
# say_hello()  # вызов функции, можно вызывать в неограниченном количестве раз.


# # Принимающая функция.
# def say_hello(name):  # принимающая функция, принимает значение, параметр.
#     print('Hello', name)
#
#
# say_hello('Arthur')
# say_hello('Rustam')
# say_hello('Timur')

# # Вызывающая функция.
# import random  # библиотека random для выбора случайного значения из списка.
#
#
# def lottery():
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)  # метод choice выбирает случайный элемент из переданного списка.
#     return win  # команда return прекращает существование функции.
#
#
# win = lottery() + lottery()  # при работе с числами можно выполнить операции по сложению, умножению, возведение в
# # степень или деление.
# print(win)
#
# # Принимающая и возвращающая.
# import random  # библиотека random для выбора случайного значения из списка.
#
#
# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(mon, thue)
#     return win1, win2
#
#
# win1, win2 = lottery('mon', 'thue')
# print(win1, win2)

# # args, kwargs
# import random  # библиотека random для выбора случайного значения из списка.
#
#
# def lottery(*args, **kwargs):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
#
# win1, win2 = lottery(1, 2, 3, 4, 5, 6)
# print(win1, win2)
#
#
# # Значения по умолчанию.
# def test(a=2, b=True):
#     print(a, b)
#
#
# test(False, 'ok')
#
#
# # Распаковка в качестве параметров список или словарь.
# def test(a=2, b=True):
#     print(a, b)
#
#
# test(*[1, 2])  # * - используется для распаковки списка. ** - для распаковки словаря.


def print_params(hh):
    print(hh, hh)


print_params('Helly Hansen')
print_params('Under Armour')
print_params('Kirgiz Miyaki')
