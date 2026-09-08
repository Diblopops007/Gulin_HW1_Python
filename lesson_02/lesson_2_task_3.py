import math

def square(x):
    return math.ceil(x * x)

side_square = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(side_square)}")