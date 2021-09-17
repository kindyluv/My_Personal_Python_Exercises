# number = [5, 6, 4, 2, 1, 9]
# max = number[0]
# for x in number:
#     if number > x:
#         x = number
# print(max)
number = [1, 1, 2, 2, 5, 7, 8, 5, 5]
# number = list(dict.fromkeys(number))
# print(number)
numbers = []
for numb in number:
    if numb not in number:
        numbers.append(numb)
print(numbers)
