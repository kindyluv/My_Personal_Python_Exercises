user = input("Enter Patient Name:  ")
user_year = int(input("Enter Birth Year: "))
user_age = 2021 - user_year
user_record = input("Enter Patient status new or old:  ")
user_colour = input("Enter Patient favourite colour:  ")
user_weight = float(input("Enter patients weight in pounds:  "))
user_kilogram = user_weight * 0.45

print(f"{user}\n{user_age} years old\n{user_record} Patient \nPatient {user} likes {user_colour}colour "
      f"\n patient weight in kg is {user_kilogram}")
