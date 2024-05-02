# age = int(input('Введите Ваш возраст '))
# if age >= 18:
#     print("OK")
# if age < 18:
#     print("NO")
# print(1 > 0)
# print(1 < 0)
# if '34' > '120':
#     print('OK')
# if '01' > '120':
#     print('OK')
# if 1 > 0:
#     print('OK')
# if [1, 1] > [2, 2]:
#     print('OK')
# if [2, 2] > [1, 2]:
#     print('OK')
# if [2, 2] <= [1, 2]:
#     print('OK')
# if [2, 2] >= [1, 2]:
#     print('OK')
# if [2, 2] == [1, 2]:  # равенство двух элементов.
#     print('OK')
# if [2, 2] != [1, 2]:  # первый элемент не равен второму.
#     print('OK')
# a = 5
# if 2 < a <=5:
#     print('OK')
# if a > 1 and a < 10:
#     print('OK')
# a = 10
# if a > 1 or a < 10:
#     print('OK')
# if a == 5 and (a > 1 or a < 10):
#     print('OK')
x = 38

print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')
# примеры
a, b = 10 ,5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех')
if (a > b) and (a > 0 or b < 1000):
    print('успех')
if 5 < b and b < 10:
    print('успех')
# можно сравнивать - числа, строки, списки.
if '34' > '123':
    print('успех')
if '123' > '12':
    print('успех')
if [1, 2] > [1, 1]:
    print('успех')
# нельзя сравнивать - разные типы.
if '6' > 5:
    print('успех')
if [5, 6] > 5:
    print('успех')
# но.
if '6' != 5:
    print('успех')
