# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099


xa = int(input("Введите координаты точки A по оси X "))
ya = int(input("Введите координаты точки A по оси Y "))
xb = int(input("Введите координаты точки B по оси X "))
yb = int(input("Введите координаты точки B по оси Y "))
from math import sqrt
print(f'Расстояние между точками A и B составляет {((xb-xa)**2+(yb-ya)**2)**0.5:.3f}')