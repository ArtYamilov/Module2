a, b, c = 59, 59, 59
if a == b == c:
    print('равносторонний')
if a == b != c:
    print('равнобедренный')
if a != b != c:
    print('разносторонний')

a, b, c = 67, 100, 54
if a >= b >= c:
    print(b)
if b >= a >= c:
    print(a)
if a >= c >= b:
    print(c)

a, b, c = 'красный', 'синий', 'желтый'
d = input('Введите два из трех основных цвета для получения вторичного: ')
if d == a + b:
    print('фиолетовый')
if d == a + c:
    print('оранжевый')
if d == b + c:
    print('зеленый')
if d != a + b and d != a + c and d != b + c:
    print('Error')
