import operator


def arithmetic():
    radius = int(input("Enter radius (2):"))
    pi = float(input("Enter pi (3.14159):"))

    diameter = operator.mul(2, radius)
    circumference = operator.mul(operator.mul(2, pi), radius)
    area = operator.pow(operator.mul(pi, radius), 2)
    result = f"the diameter is equal to {diameter}\n the circumference is equal to {circumference}\n the area is " \
             f"equal to {area} "
    print(result)


arithmetic()
