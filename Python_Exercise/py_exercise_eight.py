import operator

sign_operator = {
    "*": operator.mul
}
current_age = int(input("Enter your current: "))
years = 90 - current_age
days = 356 * years
week = 52 * years
month = 12 * years
future_age_days = days
future_age_weeks = week
future_age_month = month
print("Remaining days to 90years is: ", future_age_days, "\n", "Remaining weeks to 90years is: ", future_age_weeks,
      "\n", "Remaining months to 90years is: ", future_age_month)
