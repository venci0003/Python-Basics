import math

figure_type = input()

a = float(input())

area = 0

if figure_type == "square":

    area = a * a
elif figure_type == "rectangle":

    b = float(input())

    area = a * b

elif figure_type == "circle":

    area = math.pi * math.pow(a, 2)

elif figure_type == "triangle":

    height = float(input())

    area = a * height / 2

if area == int(area):

    print(int(area))

else:

    print(round(area * 1000) / 1000)
