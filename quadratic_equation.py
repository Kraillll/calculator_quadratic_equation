from fontTools.misc.cython import returns
from mpmath.math2 import math_sqrt
from sympy import symbols, Eq, solve
import math
import cmath


x = symbols('x')
print(f"Введите индекс a (записывайте вместе со знаком)*: ", end="")
a = input()
a = int(a)
print(f"Введите индекс b (записывайте вместе со знаком)*: ", end="")
b = input()
b = int(b)
print(f"Введите индекс c (записывайте вместе со знаком)*: ", end="")
c = input()
c = int(c)

D = b**2-4*a*c
print("Дискриминант равен:", D)


if D < 0:
    print("Квадратный корень из дискриминанта равен: ", (cmath.sqrt(D)))
    print("Дискриминант являеться отрицательным, без использования комплексных числе извлечь корни невозможно, вы хотите продолжить? (Напишите 1, если хотите продолжить, 2, если нет.)")
    yn = input()

    if yn == "1":
        x1 = (-b + (cmath.sqrt(D))) / (2 * a)
        x2 = (-b - (cmath.sqrt(D))) / (2 * a)
        print("Корни квадратного уравнения: ", x1, x2, end="")

    if yn == "2":
        print("Уравнение нерешаемо (без использования комплексных чисел)")


if (D > 0):
    print("Квадратный корень из дискриминанта равен: ", (math.sqrt(D)))
    x1 = (-b + (math.sqrt(D))) / (2 * a)
    x2 = (-b - (math.sqrt(D))) / (2 * a)
    print("x1: ", x1, end="\n")
    print("x2: ", x2)
