price = 1000000
good_credit = True
high_income = True
if good_credit and high_income:
    down_payment = 1.0 * price
    print(f"eligible for loan")
else:
    down_payment = 2.0 * price
    print(f"ineligible for loan")
    print(f"down payment is {down_payment}")
