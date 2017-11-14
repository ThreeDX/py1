import math

__author__ = 'Dmitry Panfilov'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

n2 = n1 = int(input('Задача-1: Введите целое число: '))

# Первый вариант
print('-- 1 --')
c = 0
while n1 > 0:
    if c < n1 % 10:
        c = n1 % 10
    n1 //= 10

print('Максимальная цифра:', c)

# Второй вариант
print('-- 2 --')
c = '0'
for num in str(n2):
    if c < num:
        c = num

print('Максимальная цифра:', c)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input('Задача-2: Введите первое число: '))
b = int(input('Введите второе число: '))

a ^= b
b ^= a
a ^= b

print("a = ", a, "b = ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

a = float(input('Задача-3: Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

d = b * b - 4 * a * c

if d < 0:
    print('Нет решений!')
elif d == 0 and a != 0:
    x1 = -b / (2 * a)
    print('X1 = X2 =', x1)
elif a != 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('X1 =', x1, 'X2 =', x2)
elif b != 0:
    x1 = -c / b
    print('X = ', x1)
else:
    print('Нет решений')
