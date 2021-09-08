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
unit = input("(L)bs or (K)g :  ")
weight = input("Enter weight:  ")
sign = input("Enter sign operator:  ")
userInput = (input("Enter weight:  "))


#r sign in sign_operator:
if unit.upper() == "L":
    converter = sign_operator[sign](weight, userInput)
    print({converter})

