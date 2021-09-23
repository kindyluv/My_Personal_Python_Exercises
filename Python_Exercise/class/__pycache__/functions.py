import math


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


print("Convert celsius to Fahrenheit.")

celsius = float(input("Enter a censius temp: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(celsius, "convert to ", fahrenheit, "fahrenheit")


def side_length(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def calculate_area(x1, y1, x2, y2, x3, y3):
    a = side_length(x1, y1, x2, y2)
    b = side_length(x2, y2, x3, y3)
    c = side_length(x3, y3, x1, y1)
    s = (1/2) * (a+b+c)
    return math.sqrt(s * (s-a) * (s-b)*(s-c))
