def rollercoaster_two():
    height = int(input("Enter height:  "))

    if height > 120:
        print("welcome to semicolon roller coaster")
        age = int(input("kindly enter your age:  "))
    if age >= 18:
        print("your ride would cost you $12")
    elif age < 18:
        print("your ride would cost you $7")
    else:
        print("sorry you are not qualified to ride the rollercoaster")


rollercoaster_two()
