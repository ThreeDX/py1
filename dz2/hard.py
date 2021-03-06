
__author__ = 'Dmitry Panfilov'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

print('-- 1 --')
equation = 'y = 12x - 4'
x = 2.5
lst = equation.split(" ")

y = float(lst[2][:-1]) * x
if lst[3] == '-':
    y -= float(lst[4])
else:
    y += float(lst[4])
print(equation, '\nx =', x, '\ny =', y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


def check_date(dt):
    if len(dt) != 10:
        return False

    parts = dt.split(".", 2)
    if len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return False

    try:
        d = int(parts[0])
        m = int(parts[1])
        y = int(parts[2])
    except TypeError:
        return False

    if 1 <= d <= 31 and 1 <= m <= 12 and 1 <= y <= 9999:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Високосный год
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            days[1] = 29

        if d <= days[m - 1]:
            return True

    return False


print('\n-- 2 --')
print('01.22.1001', check_date('01.22.1001'))
print('1.12.1001', check_date('1.12.1001'))
print('-2.10.3001', check_date('-2.10.3001'))
print('01.11.1985', check_date('01.11.1985'))
print('29.02.2000', check_date('29.02.2000'))
print('29.02.1900', check_date('29.02.1900'))

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

print('\n-- 3 --')
room = int(input('Введите номер комнаты: '))
block = 0
max_block_room = 0

while room > max_block_room + (block + 1) ** 2:
    block += 1
    max_block_room += block ** 2

room = room - max_block_room - 1
floor = (1 + block) * block // 2 + room // (block + 1) + 1
position = room % (block + 1) + 1

print(floor, position)
