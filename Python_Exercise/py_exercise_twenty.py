def leap_year_one():
    year = int(input("Enter year:  "))

    if year % 4 == 0:
        print(f"{year} a leap year")
        if year % 100 == 0:
            print(f"{year} is not a leap year")
        else:
            print(f"{year} a leap year")
            if year % 400 == 0:
                print(f"{year} a leap year")
            else:
                print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is not a leap year")
#
#
# leap_year_one()
