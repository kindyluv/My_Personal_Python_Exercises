def collatz(number_) -> int:
    if type(number_) == int:
        if number_ % 2 == 0:
            value = number_ // 2
            print(value)
            return value
        elif number_ % 2 != 0:
            value = 3 * number_ + 1
            print(value)
            return value
    else:
        raise ValueError


# try:
#
# except ValueError:
#     print('invalid input please a valid digit. ')
user_input = int(input('Enter an integer number \n'))

number = collatz(user_input)
while number != 1:
    number = collatz(number)
    if number == 1:
        break

