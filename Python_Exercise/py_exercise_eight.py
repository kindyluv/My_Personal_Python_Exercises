import operator

sign_operator = {
    "*": operator.mul
}
current_age = int(input("Enter your current: "))
years = 90 - current_age
days = 356 * years
week = 52 * years
month = 12 * years
print(f"You have {days} days, {week} weeks, {month} months, and {years} years left")
