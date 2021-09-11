def user_bmi():
    weight = float(input("Enter weight in m:  "))
    height = float(input("Enter height in kg:  "))

    bmi = weight/height**2
    if bmi < 18.5:
        print(f"your bmi is {bmi} so you are underweight.")
    elif 18.5 < bmi < 25:
        print(f"your bmi is {bmi} so you are  normal weight.")
    elif 25 < bmi < 30:
        print(f"your bmi is {bmi} so you are  overWeight.")
    elif 30 < bmi < 35:
        print(f"your bmi is {bmi} so you are  obese.")
#     else:
#         print(f"your bmi is {bmi} so you are  clinically obese.")
#
#
# user_bmi()
