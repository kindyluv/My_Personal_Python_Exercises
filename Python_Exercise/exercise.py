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


# number3
def multiple(list_):
    print(math.prod(list_))

# number4
def reverse_a_string(name):
    print(name[::-1])

# number5
def factorial(number):
    print(math.factorial(number))

# number 6
def number_fall(list):
    for numb in range(1, 7):
        if 3 in list:
            print(list[numb])

# number 7
def string_uppercase_lowercase():
    global c
    name = input("Enter name:  ")

    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in name:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
    print("the original input is: ", c, "\n", "the number of upper case is: ", d["UPPER_CASE"], "\n",
          "the number of lower case is: ", d["LOWER_CASE"])

# number 8
def unique_element(list_):
    unique_list = []
    for numb in list_:
        if numb not in unique_list:
            unique_list.append(numb)
    result = f"sample list is {list_}, the unique list is: {unique_list}"
    print(result)

# number 9
def prime_number(number):
    number_divisors = []
    for numb in range(1, number):
        if number % numb == 0:
            number_divisors.append(numb)

    if len(number_divisors) == 1:
        print("number is a prime number")
    else:
        print("number is not a prime number")

