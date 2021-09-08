import operator

sign_operator = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": operator.pow,
    "%": operator.mod,
    "^": operator.xor,
}
answer = 0
user = int(input("Enter first number:  "))
signs_operator = input("Enter an operator:  ")
user_two = int(input("Enter second number:  "))

if signs_operator in sign_operator.keys():
    answer = sign_operator[signs_operator](user, user_two)
    print(answer)

while True:

    signs_operator = input("Enter an operator:  ")
    if signs_operator == 'exit':
        print("final answer is: ", {answer})
        break
    user_three = int(input("Enter Number:  "))

    if signs_operator in sign_operator.keys():
        answer = sign_operator[signs_operator](answer, user_three)
        print(answer)
