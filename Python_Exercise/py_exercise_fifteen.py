def odd_or_even():
    number = int(input("Enter number:  "))
    if number % 2 == 0:
        print(f"{number} is an even number")
    elif number % 2 != 0:
        print(f"{number} is an odd number")


odd_or_even()
