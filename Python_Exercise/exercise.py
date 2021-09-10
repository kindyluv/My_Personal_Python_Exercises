import math


# number1
def maximum_of_three_numbers():
    number_0ne = int(input("Enter first number:  "))
    number_two = int(input("Enter second number:  "))
    number_three = int(input("Enter third number: "))

    get_maximum_number = max(number_0ne, number_two, number_three)
    get_minimum_number = min(number_0ne, number_two, number_three)
    print("The Maximum number is ", get_maximum_number)
    print("The minimum number is ", get_minimum_number)


# number2
def sum_number(list):
    sum = 0
    for numb in list:
        sum += numb
        print(numb)




