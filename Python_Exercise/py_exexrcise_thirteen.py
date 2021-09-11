def calculator_tip():
    print("Welcome to the tip calculator")
    total_bill = float(input("What was the total bill?:  "))
    percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?:  "))
    people = int(input("How many people are to split the bill?:  "))

    percentage_tip = percentage_tip / 100
    total_bills = total_bill * percentage_tip
    total_bill += total_bills
    people = total_bill / people
    print(f"Each person should pay ${people}")


calculator_tip()
