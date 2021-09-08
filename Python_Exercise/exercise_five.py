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

x = int(input("Enter number:  "))
sign = input("Enter sign:  ")
y = int(input("Enter number:  "))

if sign in sign_operator.keys():
    answer = sign_operator[sign](x, y)
    print(answer)

sign = input("Enter sign:  ")
z = int(input("Enter number:  "))

if sign in sign_operator.keys():
    answer = sign_operator[sign](answer, z)
    print(answer)

sign = input("Enter sign:  ")
w = int(input("Enter number:  "))

if sign in sign_operator.keys():
    answer = sign_operator[sign](answer, w)
    print(answer)
