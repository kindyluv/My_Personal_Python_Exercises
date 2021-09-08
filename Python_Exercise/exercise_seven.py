import operator

sign_operator = {
    "**": operator.pow,
    "/": operator.truediv,
    "-": operator.sub,
    "+": operator.add,
    "*": operator.mul,
    "%": operator.mod,
}

is_a_good_credit = True
price = int(input("Enter number:  "))
percent = input("Enter operator sign:  ")
user_percent = input("Enter percentage:  ")

for percent in sign_operator.keys():
    if is_a_good_credit:
      answer = percent, user_percent, price
      print(answer)
    elif not is_a_good_credit:
     answer = percent, user_percent, price
     print(answer)
else:
    print("Null")
