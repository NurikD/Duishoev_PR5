r = float(input("Введите радиус конуса:"))
h = float(input("Введите высоту конуса:"))
l = float(input("Введите апофему конуса:"))
import math
pi = math.pi
v = 1/3*pi*r**(2)*h
s = 1/3*pi*r*l
print("Объём конуса равен", v)
print("Площадь боковой поверхности равна", s)