import operator


def age():
    global years, days, week, month
    sign_operator = {
        "*": operator.mul,
    }
    signs_operator = {
        "-": operator.sub,
    }
    for sign in sign_operator:
        future_age = int(input("Enter your future age: "))
        current_age = int(input("Enter your current age: "))
        years = sign_operator[sign](future_age, current_age)
    for signs in signs_operator:
        days = signs_operator[signs](365, years)
        week = signs_operator[signs](52, years)
        month = signs_operator[signs](12, years)
    result = f"You have {days} days, {week} weeks, {month} months, and {years} years left"
    print(result)


age()

